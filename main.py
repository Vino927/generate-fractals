#!/usr/bin/env python3
# main.py
# Copyright (C) [2024] [Vino Gupta]
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, see <https://www.gnu.org/licenses>.
# Additional permission under GNU GPL version 3 section 7
# If you modify this Program, or any covered work, by linking or combining it with generate_fractals (or a modified version of that library), containing parts covered by the terms of GPL v3.0, the licensors of this Program grant you additional permission to convey the resulting work. {Corresponding Source for a non-source form of such a combination shall include the source code for the parts of generate_fractals used as well as that of the covered work.}


from matplotlib import pyplot as plt
from fractal_fern import FractalFern
from seashell import DoubleSeashell
from fractal_tree import FractalTree3D
from utils import rotate_points
import numpy as np
def main():
    # Create figures for each plot
    fig1, ax1 = plt.subplots(figsize=(5, 7))

    fig2 = plt.figure(figsize=(8, 6))
    ax2 = fig2.add_subplot(111, projection='3d')

    fig3 = plt.figure(figsize=(8, 6))
    ax3 = fig3.add_subplot(111, projection='3d')
                           
    # Plot Fractal Fern in the 1st subplot
    fern = FractalFern(100000)
    fern.generate_points()  
    fern.plot(ax=ax1)  

    # Plot Double Seashell in the 2nd subplot
    seashell = DoubleSeashell(a=0.1, b=0.2, c=0.15, n_turns=10, n_turns_inv=5, thickness=0.05, points=8000)
    seashell.generate_points() 
    seashell.plot(ax=ax2) 

    # Plot Fractal Tree in the 3rd subplot
    tree = FractalTree3D(base=np.array([0, 0, 0]), length=1, direction=np.array([0.001, 0.001, 1]), depth=7, branch_angle=np.pi / 4, scale_factor=0.5)
    tree.generate_points()  
    tree.plot(ax=ax3, set_limits=True, view_init_elev=10, view_init_azim=60)  
 
    plt.show()
    plt.close('all')


if __name__ == "__main__":
    main()