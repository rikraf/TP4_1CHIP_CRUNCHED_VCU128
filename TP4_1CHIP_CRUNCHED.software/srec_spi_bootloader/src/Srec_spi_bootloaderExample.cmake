set(OSPIPSV_NUM_DRIVER_INSTANCES "")
set(SPI_NUM_DRIVER_INSTANCES "")
set(ddr4_0_memory_0 "0x80000000;0x40000000")
set(microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0 "0x0;0x100000")
set(axi_bram_ctrl_gain_memory_0 "0xc0000000;0x80000")
set(axi_bram_ctrl_offset_memory_1 "0xc2000000;0x80000")
set(DDR ddr4_0_memory_0)
set(CODE ddr4_0_memory_0)
set(DATA ddr4_0_memory_0)
set(TOTAL_MEM_CONTROLLERS "ddr4_0_memory_0;microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0;axi_bram_ctrl_gain_memory_0;axi_bram_ctrl_offset_memory_1")
set(MEMORY_SECTION "MEMORY
{
	ddr4_0_memory_0 : ORIGIN = 0x80000000, LENGTH = 0x40000000
	microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0 : ORIGIN = 0x0, LENGTH = 0x100000
	axi_bram_ctrl_gain_memory_0 : ORIGIN = 0xc0000000, LENGTH = 0x80000
	axi_bram_ctrl_offset_memory_1 : ORIGIN = 0xc2000000, LENGTH = 0x80000
}")
set(STACK_SIZE 0x400)
set(HEAP_SIZE 0x0)
