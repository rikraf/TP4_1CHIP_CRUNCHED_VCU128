# 2026-09-08T13:53:33.403535024
import vitis

client = vitis.create_client()
client.set_workspace(path="TP4_1CHIP_CRUNCHED.software")

client.delete_component(name="memory_tests")

comp = client.create_app_component(name="memory_tests",platform = "$COMPONENT_LOCATION/../platform/export/platform/platform.xpfm",domain = "standalone_microblaze_riscv_0",template = "memory_tests")

comp = client.get_component(name="memory_tests")
status = comp.clean()

platform = client.get_component(name="platform")
status = platform.build()

comp.build()

comp = client.get_component(name="TP4_service")
status = comp.clean()

status = platform.build()

comp.build()

component = client.get_component(name="TP4_service")

lscript = component.get_ld_script(path="/home/richardraffanti/xilproj/TP4_1CHIP_CRUNCHED/TP4_1CHIP_CRUNCHED.software/TP4_service/src/lscript.ld")

lscript.regenerate()

lscript.update_ld_section(".text.init", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".heap", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.update_ld_section(".stack", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

lscript.set_stack_size("0x2000")

lscript.set_heap_size("0x2000")

status = platform.build()

comp.build()

lscript.update_ld_section(".text", "microblaze_riscv_0_local_memory_dlmb_bram_if_cntlr_memory_0")

status = comp.clean()

status = platform.build()

comp.build()

status = comp.clean()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

lscript.set_heap_size("0x20000")

status = platform.build()

comp.build()

status = platform.build()

comp.build()

comp = client.create_app_component(name="srec_spi_bootloader",platform = "$COMPONENT_LOCATION/../platform/export/platform/platform.xpfm",domain = "standalone_microblaze_riscv_0",template = "srec_spi_bootloader")

lscript.update_ld_section(".text.init", "ddr4_0_memory_0")

lscript.update_ld_section(".text", "ddr4_0_memory_0")

status = platform.build()

comp.build()

status = platform.build()

comp = client.get_component(name="srec_spi_bootloader")
comp.build()

vitis.dispose()

