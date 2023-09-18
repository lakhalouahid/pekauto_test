import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# author: O. Lak-hal


if __name__ == "__main__":
    
    ### 
    # Read csv file "data.csv"
    ###

    df = pd.read_csv("data.csv", sep=", ")

    time_s = df["time_s"].values
    x_mm = df["x_mm"].values
    y_mm = df["y_mm"].values
    roll_deg = df["roll_deg"].values
    pitch_deg = df["pitch_deg"].values

    ###
    # Plot the data
    ###


    # plots all in one subplot
    plt.figure()
    plt.subplot(2, 2, 1)
    plt.plot(x_mm, y_mm, "b-")
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.grid(True)
    plt.savefig("x-y plot.png")

    plt.subplot(2, 2, 2)
    plt.plot(time_s, roll_deg, "b-")
    plt.xlabel("time (s)")
    plt.ylabel("roll (deg)")
    plt.title("roll plot")
    plt.grid(True)
    plt.savefig("roll plot.png")

    plt.subplot(2, 2, 3)
    plt.plot(time_s, pitch_deg, "b-")
    plt.xlabel("time (s)")
    plt.ylabel("pitch (deg)")
    plt.title("pitch plot")
    plt.grid(True)
    plt.savefig("pitch plot.png")





    ###
    # Compute the projection of the gnss module post on the moving plane
    # xr_pro = 1500 * sin(pitch) * cos(roll)
    # yr_pro = 1500 * sin(pitch) * sin(roll)
    ###

    xr_pro = 1500 * np.sin(pitch_deg) * np.cos(roll_deg)
    yr_pro = 1500 * np.sin(pitch_deg) * np.sin(roll_deg)

    x_pro = x_mm + xr_pro
    y_pro = y_mm + yr_pro
    

    # Plot the x_pro-y_pro and x-y plots
    plt.figure()
    plt.plot(x_pro, y_pro, "b-", label="x_pro-y_pro")
    plt.plot(x_mm, y_mm, "r-", label="x-y")
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()


    ###
    # Compute the vehicle heading
    # heading = atan2(delta y_pro, delta x_pro)
    ###


    delta_xmm = np.diff(x_mm)
    delta_ymm = np.diff(y_mm)
    heading = np.arctan2(delta_ymm, delta_xmm) * 180 / np.pi

    # Plot the heading
    plt.figure()
    plt.plot(time_s[:-1], heading, "b-")
    plt.xlabel("time (s)")
    plt.ylabel("heading (deg)")
    plt.title("heading plot")
    plt.grid(True)
    plt.show()
    plt.savefig("heading plot.png")
