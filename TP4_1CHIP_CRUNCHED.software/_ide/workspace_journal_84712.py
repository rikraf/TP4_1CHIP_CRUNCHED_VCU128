# 2026-09-08T12:10:37.116362473
import vitis

client = vitis.create_client()
client.set_workspace(path="TP4_1CHIP_CRUNCHED.software")

comp = client.get_component(name="memory_tests")
status = comp.clean()

platform = client.get_component(name="platform")
status = platform.build()

comp.build()

status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../../TP4_1CHIP_CRUNCHED.hw_export/design_1_wrapper_04.xsa")

status = platform.build()

status = comp.clean()

status = platform.build()

comp.build()

vitis.dispose()

