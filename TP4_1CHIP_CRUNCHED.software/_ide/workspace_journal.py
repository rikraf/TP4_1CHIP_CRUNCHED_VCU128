# 2026-09-18T16:00:31.606492427
import vitis

client = vitis.create_client()
client.set_workspace(path="TP4_1CHIP_CRUNCHED.software")

component = client.get_component(name="TP4_service")

lscript = component.get_ld_script(path="/home/richardraffanti/xilproj/TP4_1CHIP_CRUNCHED/TP4_1CHIP_CRUNCHED.software/TP4_service/src/lscript.ld")

lscript.update_ld_section(".text", "ddr4_0_memory_0")

lscript.update_ld_section(".text.init", "ddr4_0_memory_0")

platform = client.get_component(name="platform")
status = platform.build()

comp = client.get_component(name="TP4_service")
comp.build()

component = client.get_component(name="srec_spi_bootloader")

lscript = component.get_ld_script(path="/home/richardraffanti/xilproj/TP4_1CHIP_CRUNCHED/TP4_1CHIP_CRUNCHED.software/srec_spi_bootloader/src/lscript.ld")

lscript.set_heap_size("0x400")

comp = client.get_component(name="srec_spi_bootloader")
status = comp.clean()

status = platform.build()

comp.build()

vitis.dispose()

