import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class OptimizationCommandHandler(Node):
    def __init__(self):
        super().__init__('optimization_command_handler')

        # Publisher to send commands to the position loader node
        self.command_publisher = self.create_publisher(String, '/commands_topic', 10)

        # Placeholder subscriber to receive commands from the optimization node
        self.optimization_subscriber = self.create_subscription(
            String,
            '/optimization_commands',
            self.optimization_callback,
            10
        )

        self.get_logger().info('OptimizationCommandHandler initialized and waiting for optimization commands')

    def optimization_callback(self, msg):
        """Callback to process commands from the optimization node."""
        self.get_logger().info(f'Received optimization commands: {msg.data}')

        # Here you can process the optimization commands if needed
        # For now, we assume the message format matches the expected command format
        processed_commands = msg.data.strip()

        # Publish the processed commands to the position loader node
        self.publish_commands(processed_commands)

    def publish_commands(self, commands):
        """Publish commands to the position loader node."""
        msg = String()
        msg.data = commands
        self.command_publisher.publish(msg)
        self.get_logger().info(f'Published commands to /commands_topic: {commands}')


def main(args=None):
    rclpy.init(args=args)
    node = OptimizationCommandHandler()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
