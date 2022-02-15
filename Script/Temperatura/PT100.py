import scipy.interpolate


class PT100:
    def __init__(self):
        res=[103.90,104.29,104.68,105.07,105.46,105.85,106.24,106.63,107.02,107.40,107.79,108.18,108.57,108.96,109.35,109.73,110.12,110.51,110.90,111.28]
        temp=[i for i in range(10,30)]
        self.interpModel=scipy.interpolate.interp1d(res,temp)

    def __call__(self, resistence, *args, **kwargs):
        return self.interpModel(resistence)