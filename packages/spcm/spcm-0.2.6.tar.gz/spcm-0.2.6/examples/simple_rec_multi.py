#
# **************************************************************************
#
# simple_rec_multi.py                                      (c) Spectrum GmbH
#
# **************************************************************************
#
# Example for all SpcMDrv based analog acquisition cards. 
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

# import spectrum driver functions
import spcm
import sys
import numpy as np
# from pyspcm import *
# from spcm_tools import *

#
# **************************************************************************
# main 
# **************************************************************************
#

# szErrorTextBuffer = create_string_buffer(ERRORTEXTLEN)
# dwError = uint32()


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

    # determine the number of channels on the card
    lNumModules = card.get(spcm.SPC_MIINST_MODULES)
    lNumChPerModule = card.get(spcm.SPC_MIINST_CHPERMODULE)
    lNumChOnCard = lNumModules * lNumChPerModule

    # do a simple standard setup
    card.set(spcm.SPC_CHENABLE,         (1 << lNumChOnCard) - 1)  # enable all channels on card
    card.set(spcm.SPC_CARDMODE,         spcm.SPC_REC_STD_MULTI)        # single trigger standard mode
    lMemsize = 1024
    card.set(spcm.SPC_MEMSIZE,          lMemsize)                 # acquire 1 kS in total
    lSegmentSize = 256
    num_segments = lMemsize // lSegmentSize
    card.set(spcm.SPC_SEGMENTSIZE,      lSegmentSize)             # ... in segments with 256 samples each
    card.set(spcm.SPC_POSTTRIGGER,      lSegmentSize // 2)                     # half of the number of samples in the segment after trigger event
    card.set(spcm.SPC_TIMEOUT,          5000)                     # timeout 5 s
    card.set(spcm.SPC_TRIG_ORMASK,      spcm.SPC_TMASK_SOFTWARE)           # software trigger
    # card.set(spcm.SPC_TRIG_EXT0_MODE,   spcm.SPC_TM_POS)               # trigger on positive edge
    # card.set(spcm.SPC_TRIG_EXT0_LEVEL0, 1500)                     # trigger at 1500mV
    card.set(spcm.SPC_TRIG_ANDMASK,     0)                        # ...
    card.set(spcm.SPC_CLOCKMODE,        spcm.SPC_CM_INTPLL)            # clock mode internal PLL

    lSetChannels = card.get(spcm.SPC_CHCOUNT)        # get the number of activated channels

    # set up the channels
    for lChannel in range(0, lSetChannels, 1):
        card.out_amp(lChannel, 1000)  # set input range to +/- 1000 mV

    card.set(spcm.SPC_SAMPLERATE, spcm.MEGA(20))

    card.set(spcm.SPC_CLOCKOUT, 0)                            # no clock output

    lBitsPerSample = card.get(spcm.SPC_MIINST_BITSPERSAMPLE)
    if lBitsPerSample <= 8:
        data_type = np.int8
    else:
        data_type = np.int16
    card.allocate_buffer(num_samples=lSegmentSize, num_segments=num_segments, sample_type=data_type)

    card.start_buffer_transfer(direction=spcm.SPCM_DIR_CARDTOPC, notify_size=0)

    # wait until the transfer has finished
    try:
        card.start(spcm.M2CMD_CARD_ENABLETRIGGER, spcm.M2CMD_DATA_WAITDMA)

        # this is the point to do anything with the data
        # e.g. calculate minimum and maximum of the acquired data
        alMin = np.min(card.buffer, axis=2)
        alMax = np.max(card.buffer, axis=2)
        for lSegment in range(num_segments):
            # print min and max for all channels in all segments
            print("Segment {}...".format(lSegment))
            print("\tChannel") 
            for lChannel in range(lSetChannels):
                print("\t{}".format(lChannel))
                print("\tMinimum: {}".format(alMin[lChannel, lSegment]))
                print("\tMaximum: {}".format(alMax[lChannel, lSegment]))
    except spcm.SpcmTimeout as timeout:
        print("Timeout...")


