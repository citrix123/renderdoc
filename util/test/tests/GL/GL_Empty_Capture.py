import renderdoc as rd
import rdtest


class GL_Empty_Capture(rdtest.TestCase):
    demos_test_name = 'GL_Empty_Capture'
    demos_frame_cap = 100

    def check_capture(self):
        draws = self.controller.GetDrawcalls()

        self.check(len(draws) == 1)
        self.check('End' in draws[0].name)
        # EID 1 is the implicit context activation
        self.check(draws[0].eventId == 2)