class Head:
    def __init__(self):
        self.description = "===This is the HEAD==="


class Hand:
    def __init__(self):
        self.description = "===This is the HAND==="


class Feet:
    def __init__(self):
        self.description = "===This is the FEET==="


class Arm:
    def __init__(self, hand):
        self.description = "===This is the ARM==="
        self.hand = hand


class Leg:
    def __init__(self, feet):
        self.description = "===This is the LEG==="
        self.feet = feet


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.description = "===This is the TORSO==="
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


class Human:
    def __init__(self, name, torso_object):
        self.name = name
        self.torso = torso_object 

    def describe_body(self):
        print(f"The Body Of: {self.name}")
        print(f"Center of the Body: {self.torso.description}")
        print(f"On Top of the Body: {self.torso.head.description}")
        print(f"Right Side: {self.torso.right_arm.description} Connected to: {self.torso.right_arm.hand.description}")
        print(f"Left Side: {self.torso.left_arm.description} Connected to: {self.torso.left_arm.hand.description}")
        print(f"At the Bottom on the Right Side: {self.torso.right_leg.description} Ending In: {self.torso.right_leg.feet.description}")
        print(f"At the Bottom on the Left Side: {self.torso.left_leg.description} Ending In: {self.torso.left_leg.feet.description}")
        print()


if __name__ == "__main__":
    my_head = Head()

    right_hand = Hand()
    left_hand = Hand()
    r_arm = Arm(right_hand)
    l_arm = Arm(left_hand)

    right_feet = Feet()
    left_feet = Feet()
    r_leg = Leg(right_feet)      
    l_leg = Leg(left_feet)

    my_torso = Torso(
        head = my_head, 
        right_arm = r_arm, 
        left_arm = l_arm, 
        right_leg = r_leg, 
        left_leg = l_leg
    )

    person = Human("Miguel", my_torso)

    person.describe_body()