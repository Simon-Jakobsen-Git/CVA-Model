import numpy as np

def discount_factors_from_short_rates(r_paths: np.ndarray, dt: float) -> np.ndarray:
    """
    Convert short-rate paths into discount factors DF(0,t) for each path.

    Inputs:
      r_paths: array shape (n_paths, n_steps+1)
      dt: time step in years

    Output:
      df_paths: array shape (n_paths, n_steps+1)
        df_paths[:, 0] = 1.0
        df_paths[:, k] = exp(-sum_{j=0}^{k-1} r[:, j] * dt)
    """
    # Integrate short rates over time: cumulative sum of r*dt
    integral = np.cumsum(r_paths[:, :-1] * dt, axis=1)  # shape (n_paths, n_steps)

    df_paths = np.empty_like(r_paths)
    df_paths[:, 0] = 1.0
    df_paths[:, 1:] = np.exp(-integral)

    return df_paths

