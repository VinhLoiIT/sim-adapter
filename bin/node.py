#!/usr/bin/python3

import rospy
from sim_adapter.dira_adapter import DiRASimAdapter
from sim_adapter.uit_adapter import UITSimAdapter
from sim_adapter.simulator import Simulator


def main():
    rospy.init_node('sim_adapter_node')
    rospy.loginfo('sim_adapter_node is initialized')
    simulator = Simulator()

    adapter = rospy.get_param('~adapter', default='dira')

    rospy.loginfo(f'Choose adapter for {adapter} simulation')

    if adapter not in ['dira', 'uit']:
        raise ValueError(f'Adapter must be in [dira, uit]')

    if adapter == 'dira':
        simulator.set_adapter(DiRASimAdapter(simulator))
    if adapter == 'uit':
        simulator.set_adapter(UITSimAdapter(simulator))

    simulator.run_loop()


if __name__ == "__main__":
    main()
