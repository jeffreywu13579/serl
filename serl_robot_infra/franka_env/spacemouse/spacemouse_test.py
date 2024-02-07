""" Test the spacemouse output. """


def test_spacemouse():
    """Test the SpaceMouseExpert class.

    This interactive test prints the action and buttons of the spacemouse at a rate of 10Hz.
    The user is expected to move the spacemouse and press its buttons while the test is running.
    It keeps running until the user stops it.

    """
    import time
    import numpy as np
    from serl_robot_infra.franka_env.spacemouse.spacemouse_expert import (
        SpaceMouseExpert,
    )

    np.set_printoptions(precision=3, suppress=True)

    spacemouse = SpaceMouseExpert()
    while True:
        action, buttons = spacemouse.get_action()
        print(f"Spacemouse action: {action}, buttons: {buttons}")
        time.sleep(0.1)


def main():
    """Call spacemouse test."""
    test_spacemouse()


if __name__ == "__main__":
    main()
