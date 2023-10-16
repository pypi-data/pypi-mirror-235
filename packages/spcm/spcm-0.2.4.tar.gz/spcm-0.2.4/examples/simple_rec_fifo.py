#
# **************************************************************************
#
# simple_rec_fifo.py                                      (c) Spectrum GmbH
#
# **************************************************************************
#
# Example for all SpcMDrv based analog acquisition cards. 
#
# Information about the different products and their drivers can be found
# online in the Knowledge Base:
# https://www.spectrum-instrumentation.com/en/platform-driver-and-series-differences
#
# Shows a simple FIFO mode example using only the few necessary commands
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

# import spectrum driver functions
import spcm
import sys
import numpy as np

#
# **************************************************************************
# main 
# **************************************************************************
#

qwTotalMem = 0
qwToTransfer = spcm.MEGA_B(8)

# settings for the FIFO mode buffer handling
qwBufferSize = spcm.MEGA_B(1)
lNotifySize = spcm.KILO_B(16)


# open card
# uncomment the second line and replace the IP address to use remote
# cards like in a digitizerNETBOX
# with spcm.Card('TCPIP::192.168.1.10::inst0::INSTR') as card:
with spcm.Card('/dev/spcm0') as card:
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

    # do a simple standard setup
    card.set(spcm.SPC_CHENABLE,       spcm.CHANNEL0)                      # just 1 channel enabled
    card.set(spcm.SPC_PRETRIGGER,     1024)                   # 1k of pretrigger data at start of FIFO mode
    card.set(spcm.SPC_CARDMODE,       spcm.SPC_REC_FIFO_SINGLE)    # single FIFO mode
    card.set(spcm.SPC_TIMEOUT,        5000)                   # timeout 5 s
    card.set(spcm.SPC_TRIG_ORMASK,    spcm.SPC_TMASK_SOFTWARE)     # trigger set to software
    card.set(spcm.SPC_TRIG_ANDMASK,   0)                      # ...
    card.set(spcm.SPC_CLOCKMODE,      spcm.SPC_CM_INTPLL)          # clock mode internal PLL

    lBitsPerSample = card.get(spcm.SPC_MIINST_BITSPERSAMPLE)

    card.set(spcm.SPC_SAMPLERATE, spcm.MEGA(20))

    card.set(spcm.SPC_CLOCKOUT, 0)                            # no clock output

    # define the data buffer
    # we try to use continuous memory if available and big enough
    card.allocate_buffer(buffer_size=qwBufferSize)

    # spcm_dwDefTransfer_i64(hCard, SPCM_BUF_DATA, SPCM_DIR_CARDTOPC, lNotifySize, pvBuffer, uint64(0), qwBufferSize)
    card.start_buffer_transfer(direction=spcm.SPCM_DIR_CARDTOPC, notify_size=lNotifySize)

    # start everything
    card.start(spcm.M2CMD_CARD_ENABLETRIGGER, spcm.M2CMD_DATA_STARTDMA)

    lMin = int(32767)   # normal python type
    lMax = int(-32768)  # normal python type
    while qwTotalMem < qwToTransfer:
        try:
            card.cmd(spcm.M2CMD_DATA_WAITDMA)
        except spcm.SpcmTimeout as timeout:
            print("... Timeout")

        lStatus = card.get(spcm.SPC_M2STATUS)
        lAvailUser = card.get(spcm.SPC_DATA_AVAIL_USER_LEN)
        lPCPos = card.get(spcm.SPC_DATA_AVAIL_USER_POS)

        if lAvailUser >= lNotifySize:
            qwTotalMem += lNotifySize
            print("Stat:{0:08x} Pos:{1:08x} Avail:{2:08x} Total:{3:.2f}MB/{4:.2f}MB".format(lStatus, lPCPos, lAvailUser, qwTotalMem / spcm.MEGA_B(1), qwToTransfer / spcm.MEGA_B(1)))

            lMin = np.min([lMin, np.min(card.buffer)])
            lMax = np.max([lMax, np.max(card.buffer)])

            card.set(spcm.SPC_DATA_AVAIL_CARD_LEN,  lNotifySize)

    # send the stop command
    dwError = card.stop(spcm.M2CMD_DATA_STOPDMA)

    print("Finished...")
    print("Minimum: {0:d}".format(lMin))
    print("Maximum: {0:d}".format(lMax))

