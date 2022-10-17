
import smbus
import time
import ctypes

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import Int32


class MinimalPublisher(Node):

	bus = smbus.SMBus(1)

	def __init__(self):
		super().__init__('minimalPublisher')
		self.publisher_velocity_ = self.create_publisher(Int32, 'velocity', 10)
		self.publisher_velocity_set_point_ = self.create_publisher(Int32, 'velocity_set_point', 10)
		self.publisher_motor_cmd_ = self.create_publisher(Int32, 'motor_cmd', 10)
		self.publisher_velocity_integral_ = self.create_publisher(Int32, 'velocity_integral', 10)
		self.publisher_velocity_erreur_ = self.create_publisher(Int32, 'velocity_erreur', 10)
		timer_period = 0.1
		self.timer = self.create_timer(timer_period, self.timer_callback)


	def get_data(self):
		data = self.bus.read_i2c_block_data(0x1E, 0x00, 18)
		position = data[0] + (data[1]<<8) + (data[2]<<16) + (data[3]<<24)
		#position = ctypes.c_int32(position).value
		switch_top = data[4]&0b1
		switch_bottom = (data[4] & 0b10)>>1
		enable = (data[4] & 0b100)>>2
		sens = (data[4] & 0b1000)>>3

		state = data[5]
		position_set_point = data[6] + (data[7]<<8) + (data[8]<<16) + (data[9]<<24)
		motor_set_point = data[0x0E]+(data[0x0F]<<8)
		motor_cmd = data[0x10]+(data[0x11]<<8)

		data = self.bus.read_i2c_block_data(0x1E, 0x40, 9)
		position_error = data[0] + (data[1]<<8) + (data[2]<<16) + (data[3]<<24)
		#position_error = ctypes.c_int32(position_error).value

		velocity_set_point = data[4]
		velocity_set_point = ctypes.c_int8(velocity_set_point).value

		velocity = data[5]+(data[6]<<8)
		velocity = ctypes.c_int16(velocity).value


		velocity_error = (data[7] + (data[8]<<8))
		velocity_error = ctypes.c_int16(velocity_error).value

		data = self.bus.read_i2c_block_data(0x1E, 0x49, 2)
		velocity_integral = (data[0] + (data[1]<<8))
		velocity_integral = ctypes.c_int16(velocity_integral).value

		msg = Int32()
		msg.data = velocity
		self.publisher_velocity_.publish(msg)

		msg_set_point = Int32()
		msg_set_point.data = velocity_set_point
		self.publisher_velocity_set_point_.publish(msg_set_point)

		msg_motor_cmd = Int32()
		msg_motor_cmd.data = motor_cmd
		self.publisher_motor_cmd_.publish(msg_motor_cmd)

		msg_velocity_integral = Int32()
		msg_velocity_integral.data = velocity_integral
		self.publisher_velocity_integral_.publish(msg_velocity_integral)

		msg_velocity_erreur = Int32()
		msg_velocity_erreur.data = velocity_error
		self.publisher_velocity_erreur_.publish(msg_velocity_erreur)

		#print(position,switch_top, switch_bottom, enable,sens, state, motor_set_point, motor_cmd, position_error, velocity_set_point, "velocity=",velocity, "velocity_error=", velocity_error)

	def timer_callback(self):
		self.get_data()

def main(args=None):
	rclpy.init(args=args)
	minimalPublisher = MinimalPublisher()
	rclpy.spin(minimalPublisher)


	minimalPublisher.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()