class StateSpaceSystem:
    def __init__(self, A, B, C, D, x0):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.x = x0

    def dot(self, M, v):
        result = []
        for row in M:
            s = 0
            for i in range(len(v)):
                s += row[i] * v[i]
            result.append(s)
        return result

    def add(self, v1, v2):
        return [v1[i] + v2[i] for i in range(len(v1))]

    def scale(self, v, scalar):
        return [scalar * v[i] for i in range(len(v))]

    def simulate(self, t_start, t_end, dt, u):
        steps = int(t_end - t_start + 1)
        x_all = []
        y_all = []

        for _ in range(steps):
            x_all.append(self.x.copy())
            y = self.dot(self.C, self.x)[0] + self.D[0][0] * u
            y_all.append(y)

            Ax = self.dot(self.A, self.x)
            Bu = self.scale([b[0] for b in self.B], u)
            dx = self.add(Ax, Bu)
            self.x = self.add(self.x, self.scale(dx, dt))

        return x_all, y_all
A = [
    [0.1, 0.2, 0.0],
    [0.0, -0.3, 0.4],
    [0.0, 0.0, -0.1]
]

B = [
    [1.0],
    [0.0],
    [0.5]
]

C = [
    [1.0, 0.0, 0.0]
]

D = [
    [0.0]
]

x0 = [0.0, 0.0, 0.0]

system = StateSpaceSystem(A, B, C, D, x0)

x_list, y_list = system.simulate(t_start=3, t_end=10, dt=1.0, u=1.0)

for i, t in enumerate(range(3, 11)):
    print("t =", t, "| x =", x_list[i], "| y =", y_list[i])
