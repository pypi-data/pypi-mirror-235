#
# **************************************************************************
#
# simple_rec_single_digital.py                             (c) Spectrum GmbH
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


import sys
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
    if lFncType in [spcm.SPCM_TYPE_DIO, spcm.SPCM_TYPE_DI]:
        print("Found: {0} sn {1:05d}\n".format(sCardName, lSerialNumber))
    else:
        print("This is an example for Digital I/O cards.\nCard: {0} sn {1:05d} not supported by example\n".format(sCardName, lSerialNumber))
        sys.exit(1) 

    #set memsize to 16 kS
    lMemsize = 16384

    # do a simple standard setup
    card.set(spcm.SPC_CHENABLE,       0xFFFF)                 # 16 bits enabled
    card.set(spcm.SPC_MEMSIZE,        lMemsize)               # acquire a total of 16k samples 
    card.set(spcm.SPC_POSTTRIGGER,    8192)                   # 8k samples after trigger event
    card.set(spcm.SPC_CARDMODE,       spcm.SPC_REC_STD_SINGLE)     # standard single acquisition mode
    card.set(spcm.SPC_TIMEOUT,        5000)                   # timeout 5 s
    card.set(spcm.SPC_TRIG_ORMASK,    spcm.SPC_TMASK_SOFTWARE)     # trigger set to software
    card.set(spcm.SPC_TRIG_ANDMASK,   0)                      # ...
    card.set(spcm.SPC_CLOCKMODE,      spcm.SPC_CM_INTPLL)          # clock mode internal PLL

    lSetChannels = card.get(spcm.SPC_CHCOUNT)         # get the number of activated channels

    # we try to set the samplerate to 20 MHz on internal PLL, no clock output
    card.set(spcm.SPC_SAMPLERATE, spcm.MEGA(20))

    card.set(spcm.SPC_CLOCKOUT, 0)                            # no clock output

    # Buffersize in bytes. Enough memory for 16384 samples with 1/8 byte each, 16 channels active
    qwBufferSize = lMemsize * lSetChannels // 8
    lNotifySize = 0  # driver should notify program after all data has been transferred

    # define the data buffer
    card.allocate_buffer(buffer_size=qwBufferSize)
    card.start_buffer_transfer(buffer_type=spcm.SPCM_BUF_DATA, direction=spcm.SPCM_DIR_CARDTOPC, notify_size=lNotifySize)

    # start everything
    try:
        card.start(spcm.M2CMD_CARD_ENABLETRIGGER, spcm.M2CMD_DATA_WAITDMA)
    except spcm.SpcmException as exception:
        print("... Timeout")

    # this is the point to do anything with the data
    # e.g. print first 10 samples to screen
    for sample in card.buffer[:10]:
        print("0b{:016b}".format(sample))


    print("Finished...")


