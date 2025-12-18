import numpy as np

def simulate_vasicek(r0, kappa, theta, sigma, dt, n_steps, seed=0):
    """
    Simulate ONE short-rate path under Vasicek.
    Returns: array shape (n_steps + 1,)
    """
    rng = np.random.default_rng(seed)
    r = np.zeros(n_steps + 1)
    r[0] = r0

    for t in range(n_steps):
        drift = kappa * (theta - r[t]) * dt
        shock = sigma * np.sqrt(dt) * rng.standard_normal()
        r[t+1] = r[t] + drift + shock

    return r

def simulate_vasicek_paths(r0, kappa, theta, sigma, dt, n_steps, n_paths, seed=0):
    """
    Simulate MANY short-rate paths under Vasicek (Monte Carlo).
    Returns: array shape (n_paths, n_steps + 1)
    """
    rng = np.random.default_rng(seed)
    r = np.zeros((n_paths, n_steps + 1))
    r[:, 0] = r0

    for t in range(n_steps):
        drift = kappa * (theta - r[:, t]) * dt                 # vector of size n_paths
        shock = sigma * np.sqrt(dt) * rng.standard_normal(n_paths)
        r[:, t+1] = r[:, t] + drift + shock

    return r


