import random
from sympy import isprime, mod_inverse


class ECCCurve:
    def _init_(self, p, a, b, g):
        self.p = p
        self.a = a
        self.b = b
        self.g = g

    def curve(self, point):
        x, y = point
        return (y*2 - x*3 - self.a * x - self.b) % self.p == 0

    def point_db(self, point):
        if point is None:
            return None
        x, y = point
        s = ((3 * x**2 + self.a) * mod_inverse(2 * y, self.p)) % self.p
        x_res = (s**2 - 2 * x) % self.p
        y_res = (s * (x - x_res) - y) % self.p
        return (x_res, y_res)

    def point_add(self, p1, p2):
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        if p1 == p2:
            return self.point_db(p1)

        x1, y1 = p1
        x2, y2 = p2
        s = ((y2 - y1) * mod_inverse(x2 - x1, self.p)) % self.p
        x_res = (s**2 - x1 - x2) % self.p
        y_res = (s * (x1 - x_res) - y1) % self.p
        return (x_res, y_res)

    def scalar_multiply(self, k, point):
        print(f"Scalar multiplication: k = {k}, point = {point}")
        result = None
        for bit in bin(k)[2:]:
            result = self.point_db(result)
            if bit == "1":
                result = self.point_add(result, point)
        return result


p = 10000000019
a = 2345678901
b = 9876543210
g = (1234567890, 987654321)


if not isprime(p):
    raise ValueError("p must be a prime number")

curve = ECCCurve(p, a, b, g)
print(f"\nCurve Parameters (p, a, b, g): {p}, {a}, {b}, {g}")

alice_pv = random.randint(1, p - 1)
bob_pvt = random.randint(1, p - 1)

print(f"\nAlice Private Key: {alice_pv}")
print(f"Bob Private Key: {bob_pvt}\n")

alice_pub = curve.scalar_multiply(alice_pv, g)
bob_pub = curve.scalar_multiply(bob_pvt, g)

print(f"\nAlice Public Key: {alice_pub}")
print(f"Bob Public Key: {bob_pub}\n")

alice_sec = curve.scalar_multiply(alice_pv, bob_pub)
bob_sec = curve.scalar_multiply(bob_pvt, alice_pub)

print("\nShared secret (Alice):", alice_sec)
print("Shared secret (Bob):", bob_sec)