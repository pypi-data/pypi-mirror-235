#
# **************************************************************************
#
# simple_rec_single-cudafft.py                             (c) Spectrum GmbH
#
# **************************************************************************
#
# Example for all SpcMDrv based analog acquisition cards and a CUDA GPU. 
#
# Information about the different products and their drivers can be found
# online in the Knowledge Base:
# https://www.spectrum-instrumentation.com/en/platform-driver-and-series-differences
#
# Shows a simple Standard mode example using only the few necessary commands
#
# Feel free to use this source for own projects and modify it in any kind
#
# Documentation for the API as well as a detailed description of the hardware
# can be found in the manual for each device which can be found on our website:
# https://www.spectrum-instrumentation.com/en/downloads
#
# Further information can be found online in the Knowledge Base:
# https://www.spectrum-instrumentation.com/en/knowledge-base-overview
#
# **************************************************************************
#

import sys
import numpy as np
import cupy
import matplotlib.pyplot as plt

# import spectrum driver functions
import spcm

#
# **************************************************************************
# main 
# **************************************************************************
#


# open card
# uncomment the second line and replace the IP address to use remote
# cards like in a digitizerNETBOX
# with spcm.Card('TCPIP::192.168.1.10::inst0::INSTR') as card:
with spcm.TimeStamp('/dev/spcm0') as card:
    if not card: sys.exit(-1)
    print("Driver version: {major}.{minor}.{build}".format(**card.drv_version()))


    # read type, function and sn and check for A/D card
    lCardType = card.get(spcm.SPC_PCITYP)
    lSerialNumber = card.sn()
    lFncType = card.get(spcm.SPC_FNCTYPE)

    sCardName = card.product_name()
    if lFncType == spcm.SPCM_TYPE_AI:
        print("Found: {0} sn {1:05d}\n".format(sCardName, lSerialNumber))
    else:
        print("This is an example for A/D cards.\nCard: {0} sn {1:05d} not supported by example\n".format(sCardName, lSerialNumber))
        exit(1)

    lNumCh = 1  # use only one channel for simplicity

    # do a simple standard setup
    lMemsize = 16384
    card.set(spcm.SPC_CHENABLE,       (1 << lNumCh) - 1)      # enable the channel
    card.set(spcm.SPC_MEMSIZE,        lMemsize)               # acquire 16 kS in total
    card.set(spcm.SPC_POSTTRIGGER,    8192)                   # half of the total number of samples after trigger event
    card.set(spcm.SPC_CARDMODE,       spcm.SPC_REC_STD_SINGLE)     # single trigger standard mode
    card.set(spcm.SPC_TIMEOUT,        5000)                   # timeout 5 s
    card.set(spcm.SPC_TRIG_ORMASK,    spcm.SPC_TMASK_SOFTWARE)     # trigger set to software
    card.set(spcm.SPC_TRIG_ANDMASK,   0)                      # ...
    card.set(spcm.SPC_CLOCKMODE,      spcm.SPC_CM_INTPLL)          # clock mode internal PLL
    card.set(spcm.SPC_CLOCKOUT,       0)                      # no clock output

    lSetChannels = card.get(spcm.SPC_CHCOUNT)      # get the number of activated channels

    # set up the channels
    lIR_mV = 1000
    for lChannel in range(0, lSetChannels, 1):
        card.out_amp(lChannel,  lIR_mV)  # set input range to +/- 1000 mV

    # we try to use the max samplerate
    llMaxSamplerate = card.get(spcm.SPC_MIINST_MAXADCLOCK)
    llSamplerate = llMaxSamplerate
    card.set(spcm.SPC_SAMPLERATE, llMaxSamplerate)
    print("Used samplerate: {0} MS/s\n".format(llSamplerate // 1000000))


    # settings for the DMA buffer
    qwBufferSize = lMemsize * 2 * lSetChannels  # in bytes. Enough memory for all samples with 2 bytes each
    lNotifySize = 0  # driver should notify program after all data has been transferred

    card.allocate_buffer(buffer_size=qwBufferSize)
    card.start_buffer_transfer(direction=spcm.SPCM_DIR_CARDTOPC, notify_size=lNotifySize)

    # start card and DMA
    try:
        dwError = card.start(spcm.M2CMD_CARD_ENABLETRIGGER)
    except spcm.SpcmTimeout as timeout:
        print("... Timeout")

    try:
        card.cmd(spcm.M2CMD_DATA_WAITDMA)
    except spcm.SpcmTimeout as timeout:
        print("... DMA Timeout")
    
    # this is the point to do anything with the data
    # e.g. calculate an FFT of the signal on a CUDA GPU
    print("Calculating FFT...")

    lMaxADCValue = card.get(spcm.SPC_MIINST_MAXADCVALUE)

    # number of threads in one CUDA block
    lNumThreadsPerBlock = 1024

    # copy data to GPU
    data_raw_gpu = cupy.array(card.buffer)

    # convert raw data to volt
    CupyKernelConvertSignalToVolt = cupy.RawKernel(r'''
        extern "C" __global__
        void CudaKernelScale(const short* anSource, float* afDest, double dFactor) {
            int i = blockDim.x * blockIdx.x + threadIdx.x;
            afDest[i] = ((float)anSource[i]) * dFactor;
        }
        ''', 'CudaKernelScale')
    data_volt_gpu = cupy.zeros(lMemsize, dtype = cupy.float32)
    CupyKernelConvertSignalToVolt((lMemsize // lNumThreadsPerBlock,), (lNumThreadsPerBlock,), (data_raw_gpu, data_volt_gpu, (lIR_mV / 1000) / lMaxADCValue))

    # calculate the FFT
    fftdata_gpu = cupy.fft.fft(data_volt_gpu)

    # length of FFT result
    lNumFFTSamples = lMemsize // 2 + 1

    # scale the FFT result
    CupyKernelScaleFFTResult = cupy.RawKernel(r'''
        extern "C" __global__
        void CudaScaleFFTResult (complex<float>* pcompDest, const complex<float>* pcompSource, int lLen) {
            int i = blockDim.x * blockIdx.x + threadIdx.x;
            pcompDest[i].real (pcompSource[i].real() / (lLen / 2 + 1)); // divide by length of signal
            pcompDest[i].imag (pcompSource[i].imag() / (lLen / 2 + 1)); // divide by length of signal
        }
        ''', 'CudaScaleFFTResult', translate_cucomplex=True)
    CupyKernelScaleFFTResult((lMemsize // lNumThreadsPerBlock,), (lNumThreadsPerBlock,), (fftdata_gpu, fftdata_gpu, lMemsize))

    # calculate real spectrum from complex FFT result
    CupyKernelFFTToSpectrum = cupy.RawKernel(r'''
        extern "C" __global__
        void CudaKernelFFTToSpectrum (const complex<float>* pcompSource, float* pfDest) {
            int i = blockDim.x * blockIdx.x + threadIdx.x;
            pfDest[i] = sqrt (pcompSource[i].real() * pcompSource[i].real() + pcompSource[i].imag() * pcompSource[i].imag());
        }
        ''', 'CudaKernelFFTToSpectrum', translate_cucomplex=True)
    spectrum_gpu = cupy.zeros(lNumFFTSamples, dtype = cupy.float32)
    CupyKernelFFTToSpectrum((lNumFFTSamples // lNumThreadsPerBlock,), (lNumThreadsPerBlock,), (fftdata_gpu, spectrum_gpu))

    # convert to dBFS
    CupyKernelSpectrumToDBFS = cupy.RawKernel(r'''
    extern "C" __global__
    void CudaKernelToDBFS (float* pfDest, const float* pfSource, int lIR_V) {
        int i = blockDim.x * blockIdx.x + threadIdx.x;
        pfDest[i] = 20. * log10f (pfSource[i] / lIR_V);
    }
    ''', 'CudaKernelToDBFS')
    CupyKernelSpectrumToDBFS((lNumFFTSamples // lNumThreadsPerBlock,), (lNumThreadsPerBlock,), (spectrum_gpu, spectrum_gpu, 1))

    spectrum_cpu = cupy.asnumpy(spectrum_gpu)  # copy FFT spectrum back to CPU
    print("done\n")

    # plot FFT spectrum
    fStep = (llSamplerate // 2) / (spectrum_cpu.size - 1)
    afFreq = np.arange(0, llSamplerate // 2, fStep)
    plt.ylim([-140, 0])  # range of Y axis
    plt.plot(afFreq, spectrum_cpu[:(spectrum_cpu.size - 1)])
    plt.show()


