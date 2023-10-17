#
# **************************************************************************
#
# simple_rec_fifo_multi_ts_poll.py                         (c) Spectrum GmbH
#
# **************************************************************************
#
# Example for all SpcmDrv digital acquisition cards. 
# Shows a simple standard mode example using only the few necessary commands
#
# Information about the different products and their drivers can be found
# online in the Knowledge Base:
# https://www.spectrum-instrumentation.com/en/platform-driver-and-series-differences
#
# Feel free to use this source for own projects and modify it in any way
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
lSegmentIndex = 0
lSegmentCnt = 0
llSamplingrate = 0

# settings for the FIFO mode buffer handling
qwBufferSize = spcm.MEGA_B(4)
lNotifySize = spcm.KILO_B(8)

qwBufferSizeTS = spcm.MEGA_B(1)
lNotifySizeTS = spcm.KILO_B(4)

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
    lFeatureMap = card.get(spcm.SPC_PCIFEATURES)

    sCardName = card.product_name()
    if lFncType == spcm.SPCM_TYPE_AI:
        print("Found: {0} sn {1:05d}\n".format(sCardName, lSerialNumber))
    else:
        print("This is an example for A/D cards.\nCard: {0} sn {1:05d} not supported by example\n".format(sCardName, lSerialNumber))
        sys.exit(1)

    if lFeatureMap & spcm.SPCM_FEAT_MULTI == 0:
        print("Multiple Recording Option not installed !\n")
        sys.exit(1)

    if lFeatureMap & spcm.SPCM_FEAT_TIMESTAMP == 0:
        print("Timestamp Option not installed !\n")
        sys.exit(1)

    lSegmentSize = 4096

    # do a simple standard setup
    card.set(spcm.SPC_CHENABLE,         1)                      # just 1 channel enabled
    card.set(spcm.SPC_PRETRIGGER,       1024)                   # 1k of pretrigger data at start of FIFO mode
    card.set(spcm.SPC_CARDMODE,         spcm.SPC_REC_FIFO_MULTI)     # multiple recording FIFO mode
    card.set(spcm.SPC_SEGMENTSIZE,      lSegmentSize)           # set segment size
    card.set(spcm.SPC_POSTTRIGGER,      lSegmentSize - 128)     # set posttrigger
    card.set(spcm.SPC_LOOPS,            0)                      # set loops
    card.set(spcm.SPC_CLOCKMODE,        spcm.SPC_CM_INTPLL)          # clock mode internal PLL
    card.set(spcm.SPC_CLOCKOUT,         0)                      # no clock output
    card.set(spcm.SPC_TRIG_EXT0_MODE,   spcm.SPC_TM_POS)             # set trigger mode
    card.set(spcm.SPC_TRIG_TERM,        0)                      # set trigger termination
    card.set(spcm.SPC_TRIG_ORMASK,      spcm.SPC_TMASK_EXT0)         # trigger set to external
    card.set(spcm.SPC_TRIG_ANDMASK,     0)                      # ...
    card.set(spcm.SPC_TRIG_EXT0_ACDC,   spcm.COUPLING_DC)            # trigger coupling
    card.set(spcm.SPC_TRIG_EXT0_LEVEL0, 1500)                   # trigger level of 1.5 Volt
    card.set(spcm.SPC_TRIG_EXT0_LEVEL1, 0)                      # unused
    card.set(spcm.SPC_TIMEOUT,          5000)                   # timeout 5 s

    lChCount = card.get(spcm.SPC_CHCOUNT)
    for lChannel in range(0, lChCount, 1):
        card.out_amp(lChannel, 1000)

    # we try to set the samplerate to 100 kHz (M2i) or 20 MHz on internal PLL, no clock output
    if ((lCardType & spcm.TYP_SERIESMASK) == spcm.TYP_M2ISERIES) or ((lCardType & spcm.TYP_SERIESMASK) == spcm.TYP_M2IEXPSERIES):
        card.set(spcm.SPC_SAMPLERATE, spcm.KILO(100))
    else:
        card.set(spcm.SPC_SAMPLERATE, spcm.MEGA(20))

    # lBitsPerSample = card.get(spcm.SPC_MIINST_BITSPERSAMPLE)
    lBytesPerSample = card.get(spcm.SPC_MIINST_BYTESPERSAMPLE)
    lBytesPerTS = 16

    # read back current sampling rate from driver
    llSamplingrate = card.get(spcm.SPC_SAMPLERATE)

    # setup timestamps
    card.ts_cmd(spcm.SPC_TSMODE_STARTRESET, spcm.SPC_TSCNT_INTERNAL)

    # open file to save timestamps
    with open('timestamps.txt', 'w') as fileTS:
        # define the data buffer
        # we try to use continuous memory if available and big enough
        card.allocate_buffer(buffer_size=qwBufferSize)
        print("!!! Using external trigger - please connect a signal to the trigger input !!!")

        ## Create second buffer
        # setup buffer for timestamps transfer
        card.allocate_ts_buffer(buffer_size=qwBufferSizeTS)
        card.start_ts_buffer_transfer(direction=spcm.SPCM_DIR_CARDTOPC, notify_size=lNotifySizeTS)

        # start everything
        card.start_buffer_transfer(direction=spcm.SPCM_DIR_CARDTOPC, notify_size=lNotifySize)
        card.start(spcm.M2CMD_CARD_ENABLETRIGGER)

        lMin = 32767  # normal python type
        lMax = -32768  # normal python type
        while qwTotalMem < qwToTransfer:
            try:
                card.set(spcm.SPC_M2CMD, spcm.M2CMD_DATA_WAITDMA)
            except spcm.SpcmTimeout as timeout:
                print("... Timeout")
            lStatus = card.get(spcm.SPC_M2STATUS)
            lAvailUser = card.get(spcm.SPC_DATA_AVAIL_USER_LEN)
            lPCPos = card.get(spcm.SPC_DATA_AVAIL_USER_POS)

            if lAvailUser >= lNotifySize:
                qwTotalMem += lNotifySize

                # this is the point to do anything with the data
                # e.g. calculate minimum and maximum of the acquired data
                lNumSamples = int(lNotifySize / 2)  # two bytes per sample
                for i in range(lPCPos // lBytesPerSample, lPCPos // lBytesPerSample + lNumSamples):
                    if card.buffer[i] < lMin:
                        lMin = card.buffer[i]
                    if card.buffer[i] > lMax:
                        lMax = card.buffer[i]

                    lSegmentIndex += 1
                    lSegmentIndex %= lSegmentSize

                    # check end of acquired segment
                    if lSegmentIndex == 0:
                        lSegmentCnt += 1

                        print("Segment[{0:d}] : Minimum: {1:d}, Maximum: {2:d}".format(lSegmentCnt, lMin, lMax))

                        lMin = 32767
                        lMax = -32768

                card.set(spcm.SPC_DATA_AVAIL_CARD_LEN, lNotifySize)

            lAvailUserTS = card.get(spcm.SPC_TS_AVAIL_USER_LEN)

            # read timestamp value(1 timestamp = 8 bytes (M2i, M3i) or 16 byte (M4i, M4x, M2p))
            if lAvailUserTS >= lBytesPerTS:

                lPCPosTS = card.get(spcm.SPC_TS_AVAIL_USER_POS)

                if (lPCPosTS + lAvailUserTS) >= qwBufferSizeTS:
                    lAvailUserTS = qwBufferSizeTS - lPCPosTS

                for i in range(lAvailUserTS // lBytesPerTS):

                    # calculate current timestamp buffer index
                    lIndex = lPCPosTS // 8 + i * lBytesPerTS // 8

                    # calculate timestamp value
                    timestampVal = card.ts_buffer[lIndex] / llSamplingrate

                    # write timestamp value to file
                    fileTS.write("{}\n".format(timestampVal))

                card.set(spcm.SPC_TS_AVAIL_CARD_LEN, lAvailUserTS)

        # send stop command
        card.stop(spcm.M2CMD_DATA_STOPDMA)

    print("Finished...")

