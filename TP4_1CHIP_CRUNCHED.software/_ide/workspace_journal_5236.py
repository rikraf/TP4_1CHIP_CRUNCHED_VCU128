# 2026-09-07T15:29:22.161988291
import vitis

client = vitis.create_client()
client.set_workspace(path="TP4_1CHIP_CRUNCHED.software")

component = client.get_component(name="memory_tests")

lscript = component.get_ld_script(path="/home/richardraffanti/xilproj/TP4_1CHIP_CRUNCHED/TP4_1CHIP_CRUNCHED.software/memory_tests/src/lscript.ld")

lscript.set_stack_size("0x2000")

lscript.set_heap_size("0x2000")

platform = client.get_component(name="platform")
status = platform.build()

comp = client.get_component(name="memory_tests")
comp.build()

vitis.dispose()

