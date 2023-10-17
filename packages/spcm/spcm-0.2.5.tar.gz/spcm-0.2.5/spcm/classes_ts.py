# -*- coding: utf-8 -*-

import numpy as np

from .regs import *
from .spcerr import *

from . import pyspcm, spcm_tools
from .pyspcm import SPCM_DIR_PCTOCARD, SPCM_DIR_CARDTOPC, SPCM_BUF_DATA, SPCM_BUF_ABA, SPCM_BUF_TIMESTAMP

from .classes import Device, Card, SpcmException, SpcmTimeout

class TimeStamp(Card):
    """a class to control Spectrum Instrumentation cards with the timestamp mode active

    For more information about what setups are available, please have a look at the user manual
    for your specific card

    Parameters
    ----------
    

    Methods
    ----------
    

    Exceptions
    ----------
    SpcmException
    SpcmTimeout
    """

    # public
    ts_buffer = None  # External numpy buffer object
    ts_buffer_size = 0

    # private
    _ts_buffer = None # Internal numpy ctypes buffer object
    _ts_buffer_alignment = 4096

    def __init__(self, device_identifier: str) -> None:
        super().__init__(device_identifier)
        #self.ts_cmd(SPC_TSMODE_STARTRESET, SPC_TSCNT_INTERNAL)
    

    def ts_cmd(self, *args) -> None:
        """
        Execute spcm timestamp commands

        Raises
        ------
        SpcmException
    
        Parameters
        ----------
        *args : int
            The different timestamp command flags to be executed.
        """

        cmd = 0
        for arg in args:
            cmd |= arg
        self.set(SPC_TIMESTAMP_CMD, cmd)

    def allocate_ts_buffer(self, buffer_size : int = None) -> None:
        """Memory allocation for the buffer that is used for communicating timestamps with the card

        Parameters
        ----------
        buffer_size : int = None
            the size of the allocated buffer in Bytes
        """

        self.ts_buffer_size = buffer_size
        item_type = np.uint64
        item_size = item_type(0).itemsize
        dwMask = self._buffer_alignment - 1

        # allocate a buffer (numpy array) for DMA transfer: a little bigger one to have room for address alignment
        databuffer_unaligned = np.empty(((self._ts_buffer_alignment + self.ts_buffer_size // item_size), ), dtype = item_type) 
        # two numpy-arrays may share the same memory: skip the begin up to the alignment boundary (ArrayVariable[SKIP_VALUE:])
        # Address of data-memory from numpy-array: ArrayVariable.__array_interface__['data'][0]
        start_pos_samples = ((self._ts_buffer_alignment - (databuffer_unaligned.__array_interface__['data'][0] & dwMask)) // item_size)
        self.ts_buffer = databuffer_unaligned[start_pos_samples:start_pos_samples + (self.buffer_size // item_size)]   # byte address but sample
        self._ts_buffer = self.ts_buffer.ctypes.data_as(pyspcm.c_void_p)
    
    def start_ts_buffer_transfer(self, *args, direction=SPCM_DIR_CARDTOPC, notify_size=0, transfer_offset=0, transfer_length=None):
        """Start the transfer of the timestamp data to the card using the M2CMD_DATA_STARTDMA command
        
        Parameters
        ----------
        *args : list
            list of additonal arguments that are added as flags to the start dma command
        """

        if transfer_length is None: transfer_length = self.ts_buffer_size
        
        # we define the buffer for transfer and start the DMA transfer
        self.print("Starting the Timestamp transfer and waiting until data is in board memory")
        pyspcm.spcm_dwDefTransfer_i64(self._handle, SPCM_BUF_TIMESTAMP, direction, notify_size, self._ts_buffer, transfer_offset, transfer_length)
        cmd = M2CMD_EXTRA_POLL
        for arg in args:
            cmd |= arg
        self.cmd(cmd)
        self.print("... timestamp data transfer started")
    pass

