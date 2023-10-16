import numpy as np
from scipy.signal import savgol_filter
from scipy import optimize
import matplotlib.pyplot as plt


def fun_log_left(x,p0,p1,p2,p3):
    result=p0+p1/(1+np.exp((-1)*p3*(x-p2)))
    return result
def fun_log_right(x,p0,p1,p2,p3):
    result=p0-p1/(1+np.exp((-1)*p3*(x-p2)))
    return result
def fun_doublelog(x, p0,p1,p2,p3,p4,p5,p6):
    result = p0 + p1 / (1 + np.exp((-1) * p5 * (x - p3))) - p2 / (1 + np.exp((-1) * p6 * (x - p4)))
    return result
def fun_doublelog_(x, p):
    p0, p1, p2, p3, p4, p5, p6=p
    result = p0 + p1 / (1 + np.exp((-1) * p5 * (x - p3))) - p2 / (1 + np.exp((-1) * p6 * (x - p4)))
    return result
def GetPheno(ar,daylist):
        ar_sg = savgol_filter(ar, 5, 1, mode='nearest')
        d=np.where(ar_sg==max(ar_sg))[0][0]
        ar_left=ar[:d]
        ar_right=ar[d:]
        ar_left_p=np.percentile(ar_left,5)
        ar_right_p = np.percentile(ar_right, 5)
        ar_up_p=np.percentile(ar,95)
        x_left = daylist[:d]
        x_right = daylist[d:]
        N=10
        fit_x_left=np.append(np.arange((-1)*N*10+x_left[0],x_left[0],10),np.append(x_left,np.arange(x_left[-1],x_left[-1]+8*N,8)))
        fit_y_left = np.append(np.array([ar_left_p]*N), np.append(ar_left, np.array([ar_up_p]*N)))
        param_bounds_left = (
            (ar_left_p-5, ar_up_p-ar_left_p-5, -np.inf, 0.030),
            (ar_left_p+5, ar_up_p-ar_left_p+5, np.inf, np.inf))
        param_bounds_right = (
            (ar_up_p-5, ar_up_p-ar_right_p-5, -np.inf, 0.030),
            (ar_up_p+5, ar_up_p-ar_right_p+5, np.inf, np.inf))
        orginvalue_left=np.array([ar_left_p,ar_up_p-ar_left_p,x_left[0]+90,0.08])
        orginvalue_right = np.array([ar_up_p, ar_up_p-ar_right_p, x_left[0]+270, 0.08])
        fit_x_right=np.append(np.append(np.arange(x_right[0]-8*N,x_right[0],8),x_right),np.arange(x_right[-1],x_right[-1]+10*N,10))
        fit_y_right =np.append(np.array([ar_up_p]*N), np.append(ar_right, np.array([ar_right_p]*N)))
        ret_left = optimize.curve_fit(fun_log_left, fit_x_left, fit_y_left, p0=orginvalue_left, xtol=1e-3, maxfev=10000,bounds=param_bounds_left)[0]
        ret_right = optimize.curve_fit(fun_log_right, fit_x_right, fit_y_right, p0=orginvalue_right, xtol=1e-3, maxfev=10000,bounds=param_bounds_right)[0]
        para1 = [ret_left[0], (ret_left[1]+ret_right[0]-ret_left[0])/2,(ret_left[1]+ret_left[0]-ret_right[0])/2+ret_right[1], ret_left[2], ret_right[2], ret_left[3], ret_right[3]]
        y_mean = np.mean(ar)
        ar_fit=fun_doublelog_(daylist,para1)
        SSE = (ar - ar_fit) ** 2
        SST = (ar - y_mean) ** 2
        R_2 = 1 - sum(SSE) / sum(SST)
        para1 = [R_2,ret_left[0], ret_left[1], ret_right[1], ret_left[2], ret_right[2], ret_left[3], ret_right[3]]

        return para1
class DoubleLogistic:
    def __init__(self,daylist,ar):
        pr = GetPheno(ar, daylist)
        self.DoyList=daylist
        self.GrowthProcess=ar
        self.Parameter=pr[1:]
        self.R_2 = pr[0]
        self.Alpha_0 = pr[1]
        self.Alpha_1 = pr[2]
        self.Alpha_2 = pr[3]
        self.Beta_1 = pr[4]
        self.Beta_2 = pr[5]
        self.Round_1 = pr[6]
        self.Round_2 = pr[7]
    def GetSOS(self):
        SOS= np.round(self.Beta_1 - 2.181 / self.Round_1)
        return SOS
    def GetEOS(self):
        EOS= np.round(self.Beta_2 + 2.181 / self.Round_2)
        return EOS
    def GetRelativeThreshold(self,Threshold):
        daylist=self.DoyList
        X_=np.arange(daylist[0],daylist[-1]+1,1)
        Y_=fun_doublelog_(X_,self.Parameter)
        max_f_index = np.where(Y_==max(Y_))[0][0]
        f_left = Y_[:max_f_index]
        f_right = Y_[max_f_index:]
        per_left_5 ,per_left_95= np.percentile(f_left, [5,95])
        per_right_5 ,per_right_95= np.percentile(f_right, [5,95])
        cha_left = np.abs((f_left - per_left_5) / (per_left_95 - per_left_5) - Threshold)
        cha_right = np.abs((f_right - per_right_5) / (per_right_95 - per_right_5) - Threshold)
        index1 =np.where(cha_left == min(cha_left))[0][0]
        index2 = np.where(cha_right == min(cha_right))[0][0] + max_f_index
        SOS_Y = (index1) + 1+X_[0]
        EOS_Y = (index2) - 2+X_[0]
        return SOS_Y,EOS_Y
    def Drawing(self):
        plt.scatter(self.DoyList,self.GrowthProcess,s=3)
        plt.plot(self.DoyList,fun_doublelog_(self.DoyList, self.Parameter))
        plt.axvline(self.GetSOS())
        plt.axvline(self.GetEOS())
        plt.show()






