/******************************************************************************
* Copyright (c) 2023 Advanced Micro Devices, Inc. All Rights Reserved.
* SPDX-License-Identifier: MIT
******************************************************************************/
#include "memory_config.h"

struct memory_range_s memory_ranges[] = {
	/* microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0 memory will not be tested since application resides in the same memory */
	{
        	"axi_bram_ctrl_gain_memory_0",
        	"axi_bram_ctrl_gain_memory_0",
        	0xc0000000,
        	0x80000,
          },
	 {
        	"axi_bram_ctrl_offset_memory_1",
        	"axi_bram_ctrl_offset_memory_1",
        	0xc2000000,
        	0x80000,
          },
	 {
        	"ddr4_0_memory_0",
        	"ddr4_0_memory_0",
        	0x80000000,
        	0x40000000,
          },
	 
};

int n_memory_ranges = 3;
