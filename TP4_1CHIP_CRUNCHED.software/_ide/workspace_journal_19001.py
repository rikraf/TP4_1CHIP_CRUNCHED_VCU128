# 2026-09-08T11:46:52.720598386
import vitis

client = vitis.create_client()
client.set_workspace(path="TP4_1CHIP_CRUNCHED.software")

client.delete_component(name="memory_tests")

platform = client.get_component(name="platform")
status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../TP4_1CHIP_CRUNCHED.hw_export/design_1_wrapper_01.xsa")

status = platform.build()

comp = client.create_app_component(name="memory_tests",platform = "$COMPONENT_LOCATION/../platform/export/platform/platform.xpfm",domain = "standalone_microblaze_riscv_0",template = "memory_tests")

status = platform.build()

comp = client.get_component(name="memory_tests")
comp.build()

status = comp.clean()

status = platform.build()

comp.build()

component = client.get_component(name="memory_tests")

lscript = component.get_ld_script(path="/home/richardraffanti/xilproj/TP4_1CHIP_CRUNCHED/TP4_1CHIP_CRUNCHED.software/memory_tests/src/lscript.ld")

lscript.set_heap_size("0x1000")

lscript.set_stack_size("0x1000")

status = comp.clean()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = comp.clean()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

vitis.dispose()

