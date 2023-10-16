import numpy as np
from astropy.io import fits
from spectral_cube import SpectralCube
from pathlib import Path
from scipy import interpolate
import numpy.random as rand
import Functions.Photon.Contamination as Cont

def fits_reading(FitsPath):
    print('Read the simulation')
    filename = Path(FitsPath).resolve()
    data = fits.open(filename)
    cube = SpectralCube.read(data)
    data.close()
    start = cube.header['CRVAL3']
    step = cube.header['CDELT3']
    stop = len(cube[:,0,0])*step+start
    wavelength = np.linspace(start,stop, len(cube[:,0,0]))*10**-3

    Spectrum_func = np.zeros(np.shape(cube[0,:,:]),dtype = object)
    Spectrum_func_value = np.zeros(np.shape(cube[0,:,:]))
    for i in range(np.shape(cube[0,:,:])[0]):
        for j in range(np.shape(cube[0,:,:])[1]):
            Spectrum_func[i,j] = interpolate.interp1d(wavelength,cube[:,i,j])
            Spectrum_func_value[i,j] = max(Spectrum_func[i,j](wavelength))

    return(wavelength,Spectrum_func,Spectrum_func_value)


def Photon_sort(Photon_number,FitsPath):
    wavelength,Spectrum_func,max_amp = fits_reading(FitsPath)
    maxim = max_amp.max()
    Photon_wv = np.zeros(np.shape(Spectrum_func),dtype = object)
    Photon_amp = np.zeros(np.shape(Spectrum_func),dtype = object)
    print('Photon creation')
    for i in range(np.shape(Spectrum_func)[0]):
        for j in range(np.shape(Spectrum_func)[1]):
            print(i,j)
            count = []
            Photon_rand = [rand.uniform(low=wavelength[0],high=wavelength[-1],size = Photon_number),rand.uniform(low = 0,high = maxim,size = Photon_number)]
            if max_amp[i,j] > 0 :
                for k in range(len(Photon_rand[0])):
                    if Photon_rand[1][k] < Spectrum_func[i,j](Photon_rand[0][k]):
                        count.append(k)
            contamination = Cont.Continuous(Photon_number*0.01,wavelength[0],wavelength[-1],0,maxim)
            Photon_wv[i,j] = list(Photon_rand[0][count]) + list(contamination[0])
            Photon_amp[i,j] = list(Photon_rand[1][count]) + list(contamination[1])
    return(Photon_wv,Photon_amp)

def detector_scale(detector_dim,Photon_wv,Photon_amp):
    Wavelength = np.zeros(detector_dim,dtype = object)
    Amplitude = np.zeros(detector_dim,dtype = object)
    x_det,y_det = detector_dim[0],detector_dim[1]
    x_im, y_im = np.shape(Photon_wv)[0], np.shape(Photon_wv)[1]
    ratio_x = int(x_im/x_det)
    ratio_y = int(y_im/y_det)
    for i in range(x_im):
        for j in range(y_im):
            if i//ratio_x < x_det and j//ratio_y < y_det:
                if  i%ratio_x == 0 and j%ratio_y == 0:
                    Wavelength[i//ratio_x, j//ratio_y] = []
                    Amplitude[i//ratio_x, j//ratio_y] = []
                Wavelength[i//ratio_x, j//ratio_y] += list(Photon_wv[i,j])
                Amplitude[i//ratio_x, j//ratio_y] += list(Photon_amp[i,j])
    
    return(Wavelength,Amplitude)
