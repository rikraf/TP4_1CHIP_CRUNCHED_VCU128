# 2026-09-11T13:40:53.303578348
import vitis

client = vitis.create_client()
client.set_workspace(path="TP4_1CHIP_CRUNCHED.software")

platform = client.get_component(name="platform")
status = platform.build()

comp = client.get_component(name="memory_tests")
comp.build()

status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../TP4_1CHIP_CRUNCHED.hw_export/design_1_wrapper_05.xsa")

status = platform.build()

comp = client.get_component(name="TP4_service")
status = comp.clean()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

component = client.get_component(name="TP4_service")

lscript = component.get_ld_script(path="/home/richardraffanti/xilproj/TP4_1CHIP_CRUNCHED/TP4_1CHIP_CRUNCHED.software/TP4_service/src/lscript.ld")

lscript.update_ld_section(".text.init", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".text", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

status = platform.build()

comp.build()

status = platform.build()

comp = client.get_component(name="srec_spi_bootloader")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

component = client.get_component(name="srec_spi_bootloader")

lscript = component.get_ld_script(path="/home/richardraffanti/xilproj/TP4_1CHIP_CRUNCHED/TP4_1CHIP_CRUNCHED.software/srec_spi_bootloader/src/lscript.ld")

lscript.update_ld_section(".text.init", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".text", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".note.gnu.build-id", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".init", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".fini", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".ctors", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".dtors", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".rodata", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".srodata", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".sdata2", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".data", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".got", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".got1", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".got2", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".eh_frame", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".jcr", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".gcc_except_table", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".init_array", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".fini_array", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".sdata", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".tdata", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".tbss", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".bss", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".sbss", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".sbss2", "ddr4_0_memory_0")

lscript.update_ld_section(".sbss2", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".heap", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".stack", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

status = platform.build()

comp.build()

vitis.dispose()

