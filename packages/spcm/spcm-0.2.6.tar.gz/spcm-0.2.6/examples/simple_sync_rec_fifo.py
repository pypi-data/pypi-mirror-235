#
# **************************************************************************
#
# simple_sync_rec_fifo.py                                  (c) Spectrum GmbH
#
# **************************************************************************
#
# Example for two synchronized SpcMDrv based analog acquisition cards.
#
# Information about the different products and their drivers can be found
# online in the Knowledge Base:
# https://www.spectrum-instrumentation.com/en/platform-driver-and-series-differences
#
# Shows a simple multi-threaded FIFO mode example using only the
# few necessary commands. The example uses only minimal error handling
# to simplify the code.
#
# Feel free to use this source for own projects and modify it in any kind.
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

import threading
import sys
import spcm

# import spectrum driver functions
# from pyspcm import *
# from spcm_tools import *

#
# **************************************************************************
# CardThread: thread that handles the data transfer for a card
# One instance will be started for each card.
# **************************************************************************
#


class CardThread (threading.Thread):
    def __init__ (self, index, card):
        threading.Thread.__init__(self)
        self.index    = index     # index of card (only used for output)
        self.card    = card     # handle to the card
        #self.m_pvBuffer = pvBuffer  # DMA buffer for the card

    def run(self):
        lMin = 32767  # normal python type
        lMax = -32768  # normal python type
        # lStatus = int32()
        # lAvailUser = int32()
        # lPCPos = int32()

        qwToTransfer = spcm.MEGA_B(8)  # card will be stopped after this amount of data has been transferred
        qwTotalMem = 0         # counts amount of already transferred data
        while qwTotalMem < qwToTransfer:
            try:
                self.card.cmd(spcm.M2CMD_DATA_WAITDMA)
            except spcm.SpcmTimeout as timeout:
                print("{} ... Timeout".format(self.index))
            # get status and amount of available data
            lStatus = self.card.get(spcm.SPC_M2STATUS)
            lAvailUser = self.card.get(spcm.SPC_DATA_AVAIL_USER_LEN)
            lPCPos = self.card.get(spcm.SPC_DATA_AVAIL_USER_POS)

            if lAvailUser >= lNotifySize:
                qwTotalMem += lNotifySize
                #print("{0} Stat:{1:08x} Pos:{2:08x} Avail:{3:08x} Total:{4:.2f}MB/{5:.2f}MB".format(self.index, lStatus, lPCPos, lAvailUser, qwTotalMem / spcm.MEGA_B(1), qwToTransfer / spcm.MEGA_B(1)))

                # this is the point to do anything with the data
                # e.g. calculate minimum and maximum of the acquired data
                # pnData = cast(addressof(self.m_pvBuffer.contents) + lPCPos, ptr16)  # cast to pointer to 16bit integer
                lNumSamples = int(lNotifySize / 2)  # two bytes per sample
                for i in range(0, lNumSamples - 1, 1):
                    if self.card.buffer[i] < lMin:
                        lMin = self.card.buffer[i]
                    if self.card.buffer[i] > lMax:
                        lMax = self.card.buffer[i]

                # mark buffer space as available again
                self.card.set(spcm.SPC_DATA_AVAIL_CARD_LEN, lNotifySize)

        # send the stop command
        self.card.stop(spcm.M2CMD_DATA_STOPDMA)

        # print the calculated results
        print("{0} Finished... Minimum: {1:d} Maximum: {2:d}".format(self.index, lMin, lMax))


#
# **************************************************************************
# main
# **************************************************************************
#


# settings for the FIFO mode buffer handling
qwBufferSize = spcm.MEGA_B(4)
lNotifySize = spcm.KILO_B(16)

card_identifiers = ["/dev/spcm0", "/dev/spcm1"]
sync_identifier  = "sync0"

# open cards and sync
with spcm.CardStack(card_identifiers=card_identifiers, sync_identifier=sync_identifier) as stack:
    if not stack: sys.exit(-1)
    for card in stack.cards:
        # read type, function and sn and check for A/D card
        lCardType = card.get(spcm.SPC_PCITYP)
        lSerialNumber = card.sn()
        lFncType = card.get(spcm.SPC_FNCTYPE)

        sCardName = card.product_name()
        if lFncType == spcm.SPCM_TYPE_AI:
            print("Found: {0} sn {1:05d}".format(sCardName, lSerialNumber))
        else:
            print("This is an example for A/D cards.\nCard: {0} sn {1:05d} not supported by example\n".format(sCardName, lSerialNumber))
            sys.exit(1)

        card.set(spcm.SPC_CHENABLE,       1)                      # just 1 channel enabled
        card.set(spcm.SPC_PRETRIGGER,     1024)                   # 1k of pretrigger data at start of FIFO mode
        card.card_mode(spcm.SPC_REC_FIFO_SINGLE)    # single FIFO mode
        card.set(spcm.SPC_TIMEOUT,        5000)                   # timeout 5 s
        card.set(spcm.SPC_TRIG_ORMASK,    spcm.SPC_TMASK_SOFTWARE)     # trigger set to software
        card.set(spcm.SPC_TRIG_ANDMASK,   0)                      # ...
        card.set(spcm.SPC_CLOCKMODE,      spcm.SPC_CM_INTPLL)          # clock mode internal PLL

        # we try to set the samplerate to 100 kHz (M2i) or 20 MHz (M3i/M4i) on internal PLL, no clock output
        card.set(spcm.SPC_SAMPLERATE, spcm.MEGA(20))

        card.set(spcm.SPC_CLOCKOUT, 0)                            # no clock output

        # define the data buffer
        # we try to use continuous memory if available and big enough
        card.allocate_buffer(buffer_size=qwBufferSize)
        card.start_buffer_transfer(direction=spcm.SPCM_DIR_CARDTOPC, notify_size=lNotifySize)


    # setup star-hub
    nCardCount = len(card_identifiers)
    stack.sync.set(spcm.SPC_SYNC_ENABLEMASK, (1 << nCardCount) - 1)

    # find star-hub carrier card and set it as clock master
    i = 0
    for card in stack.cards:
        lFeatures = card.get(spcm.SPC_PCIFEATURES)
        if lFeatures & (spcm.SPCM_FEAT_STARHUB5 | spcm.SPCM_FEAT_STARHUB16):
            break
        i += 1
    stack.sync.set(spcm.SPC_SYNC_CLKMASK, (1 << i))


    # start all cards using the star-hub handle
    stack.sync.start(spcm.M2CMD_CARD_ENABLETRIGGER, spcm.M2CMD_DATA_STARTDMA)

    # for each card we start a thread that controls the data transfer
    listThreads = []
    i = 0
    for card in stack.cards:
        thread = CardThread(i, card)
        listThreads += [thread]
        thread.start()
        i = i + 1

    # wait until all threads have finished
    for x in listThreads:
        x.join()

