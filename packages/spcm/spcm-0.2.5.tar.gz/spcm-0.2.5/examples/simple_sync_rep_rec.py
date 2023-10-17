#
# **************************************************************************
#
# simple_sync_rep_rec.py                                  (c) Spectrum GmbH
#
# **************************************************************************
#
# Information about the different products and their drivers can be found
# online in the Knowledge Base:
# https://www.spectrum-instrumentation.com/en/platform-driver-and-series-differences
#
# Shows a simple example using synchronized replay and record
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
import msvcrt

import spcm

def lKbhit():
    return ord(msvcrt.getch()) if msvcrt.kbhit() else 0


#
# **************************************************************************
# Setup AD card
# **************************************************************************
#

def vSetupCardAD(card : spcm.Card):
    # set up the mode
    card.set(spcm.SPC_CARDMODE, spcm.SPC_REC_FIFO_SINGLE)
    card.set(spcm.SPC_PRETRIGGER, 8)
    card.set(spcm.SPC_CHENABLE, spcm.CHANNEL0)

    # setup trigger
    card.set(spcm.SPC_TRIG_ORMASK, spcm.SPC_TMASK_SOFTWARE)
    card.set(spcm.SPC_TRIG_ANDMASK, 0)
    card.set(spcm.SPC_TRIG_CH_ORMASK0, 0)
    card.set(spcm.SPC_TRIG_CH_ORMASK1, 0)
    card.set(spcm.SPC_TRIG_CH_ANDMASK0, 0)
    card.set(spcm.SPC_TRIG_CH_ANDMASK1, 0)
    card.set(spcm.SPC_TRIGGEROUT, 0)

    # set up clock
    card.set(spcm.SPC_CLOCKMODE, spcm.SPC_CM_INTPLL)
    card.set(spcm.SPC_SAMPLERATE, spcm.MEGA(5))

    card.set(spcm.SPC_TIMEOUT, 5000)

    # set up the channels
    lNumChannels = card.get(spcm.SPC_CHCOUNT)
    for lChannel in range(lNumChannels):
        card.out_amp(lChannel, 1000)


#
# **************************************************************************
# Setup DA card
# **************************************************************************
#

def vSetupCardDA(card : spcm.Card):
    llMemSamples = spcm.KILO_B(64)

    card.card_mode(spcm.SPC_REP_STD_CONTINUOUS)
    card.set(spcm.SPC_CHENABLE, spcm.CHANNEL0)
    card.set(spcm.SPC_MEMSIZE, llMemSamples)
    card.set(spcm.SPC_LOOPS, 0)

    card.set(spcm.SPC_CLOCKMODE, spcm.SPC_CM_INTPLL)
    card.set(spcm.SPC_SAMPLERATE, spcm.MEGA(50))
    card.set(spcm.SPC_CLOCKOUT, 0)

    card.set(spcm.SPC_TRIG_ORMASK, spcm.SPC_TMASK_SOFTWARE)
    card.set(spcm.SPC_TRIG_ANDMASK, 0)
    card.set(spcm.SPC_TRIG_CH_ORMASK0, 0)
    card.set(spcm.SPC_TRIG_CH_ORMASK1, 0)
    card.set(spcm.SPC_TRIG_CH_ANDMASK0, 0)
    card.set(spcm.SPC_TRIG_CH_ANDMASK1, 0)
    card.set(spcm.SPC_TRIGGEROUT, 0)

    lSetChannels = card.get(spcm.SPC_CHCOUNT)

    for lChannel in range(lSetChannels):
        card.out_enable(lChannel, 1)
        card.out_amp(lChannel, 1000)
        card.out_stop_level(lChannel, spcm.SPCM_STOPLVL_HOLDLAST)

    # allocate buffer for data transfer
    card.allocate_buffer(num_samples=llMemSamples)

    # calculate sine waveform
    sample_space = np.arange(llMemSamples)
    card.buffer = np.int16(5000 * np.sin(2.0 * np.pi * sample_space / llMemSamples))

    # we define the buffer for transfer and start the DMA transfer
    print("Starting the DMA transfer and waiting until data is in board memory\n")
    card.start_buffer_transfer(spcm.M2CMD_DATA_WAITDMA, direction=spcm.SPCM_DIR_PCTOCARD)
    print("... data has been transferred to board memory\n")


#
# **************************************************************************
# main
# **************************************************************************
#

lMBytesToAcquire = 100

# settings for the FIFO mode buffer handling
llBufferSizeInBytes = spcm.MEGA_B(8)
lNotifySize = spcm.KILO_B(16)

# szErrorTextBuffer = create_string_buffer(ERRORTEXTLEN)

# open cards
card_identifiers = ["/dev/spcm0", "/dev/spcm1"]
sync_identifier  = "sync0"

# open cards and sync
with spcm.CardStack(card_identifiers=card_identifiers, sync_identifier=sync_identifier) as stack:
    if not stack: sys.exit(-1)
    card_DA = None
    card_AD = None
    for card in stack.cards:
        # read type, function and sn and check for A/D card
        lCardType = card.get(spcm.SPC_PCITYP)
        lSerialNumber = card.sn()
        lFncType = card.get(spcm.SPC_FNCTYPE)

        sCardName = card.product_name()

        if lFncType == spcm.SPCM_TYPE_AO:
            card_DA = card
            print("DA card found: {0} sn {1:05d}".format(sCardName, lSerialNumber))
        else:
            card_AD = card
            print("AD card found: {0} sn {1:05d}".format(sCardName, lSerialNumber))

    if card_DA == None or card_AD == None:
        print("Invalid cards ...")
        sys.exit(1)

    # setup DA card
    vSetupCardDA(card_DA)

    # setup AD card
    vSetupCardAD(card_AD)

    # setup star-hub
    stack.sync.set(spcm.SPC_SYNC_ENABLEMASK, 3)
    stack.sync.set(spcm.SPC_SYNC_CLKMASK, 1)

    # buffer settings for Fifo transfer
    card_AD.allocate_buffer(buffer_size=llBufferSizeInBytes)
    card_AD.start_buffer_transfer(direction=spcm.SPCM_DIR_CARDTOPC, notify_size=lNotifySize)

    stack.sync.start(spcm.M2CMD_CARD_ENABLETRIGGER)

    print("Acquisition stops after {} MBytes are transferred".format(lMBytesToAcquire))

    print("Press ESC to stop")

    qwTotalMem = 0
    plotData = np.array([], dtype=np.int16)

    while True:

        if qwTotalMem >= spcm.MEGA_B(lMBytesToAcquire):
            break

        lKey = lKbhit()
        if lKey == 27:  # ESC
            stack.sync.stop()
            break
        else:
            # get status and amount of available data
            lStatus = card_AD.get(spcm.SPC_M2STATUS)
            lAvailUser = card_AD.get(spcm.SPC_DATA_AVAIL_USER_LEN)
            lPCPos = card_AD.get(spcm.SPC_DATA_AVAIL_USER_POS)

            if lAvailUser >= lNotifySize:
                qwTotalMem += lNotifySize

                print("Total:{} MB".format(qwTotalMem / spcm.MEGA_B(1)))

                # save first block to plot later
                if lPCPos == 0 and len(plotData) == 0:
                    print(card_AD.buffer[lPCPos : (lPCPos + lNotifySize)])
                    plotData = np.concatenate((plotData, card_AD.buffer[lPCPos : (lPCPos + lNotifySize)]))

                card_AD.set(spcm.SPC_DATA_AVAIL_CARD_LEN, lNotifySize)

            # wait for next block
            card_AD.cmd(spcm.M2CMD_DATA_WAITDMA)

    stack.sync.stop()
    # spcm_dwSetParam_i32(hSync, SPC_M2CMD, M2CMD_CARD_STOP)

    # close sync handle
    # spcm_vClose(hSync)

    # # close cards
    # spcm_vClose(hCardAD)
    # spcm_vClose(hCardDA)

    # plot first data block
    # plt.plot(plotData)
    # plt.show()
