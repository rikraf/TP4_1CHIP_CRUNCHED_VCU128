# 2026-09-07T10:44:03.099249663
import vitis

client = vitis.create_client()
client.set_workspace(path="TP4_1CHIP_CRUNCHED.software")

platform = client.get_component(name="platform")
status = platform.build()

comp = client.get_component(name="TP4_service")
status = comp.clean()

status = platform.build()

comp.build()

status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../TP4_1CHIP_CRUNCHED.hw_export/design_1_wrapper_03.xsa")

status = platform.build()

status = comp.clean()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

domain = platform.get_domain(name="standalone_microblaze_riscv_0")

status = domain.regenerate()

status = platform.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = comp.clean()

status = platform.build()

comp.build()

status = platform.build()

status = comp.clean()

status = platform.build()

comp.build()

status = comp.clean()

status = platform.build()

comp.build()

comp = client.create_app_component(name="memory_tests",platform = "$COMPONENT_LOCATION/../platform/export/platform/platform.xpfm",domain = "standalone_microblaze_riscv_0",template = "memory_tests")

status = platform.build()

comp = client.get_component(name="memory_tests")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = comp.clean()

status = platform.build()

comp.build()

vitis.dispose()

