import numpy as np

def get_weight(indicator_vec):

    weight_vec = indicator_vec
    weight_arr = np.array(weight_vec)
    weight2_arr = weight_arr**2 # weight square

    return weight_arr, weight2_arr

def init_guess(all_ds, all_ps, all_hs, all_w2):

    total_w2 = np.sum(all_w2)

    init_d = np.sum(all_w2*all_ds)/total_w2
    init_p = np.sum(all_w2*all_ps)/total_w2
    init_h = np.sum(all_w2*all_hs)/total_w2

    return init_d, init_p, init_h

def get_distance(dm, pm, hm, ds, ps, hs):

    distance = np.sqrt(4*(dm-ds)**2+(pm-ps)**2+(hm-hs)**2)

    return distance

def get_delta(dm, pm, hm, all_ds, all_ps, all_hs, all_w, alpha):

    all_r = get_distance(dm, pm, hm, all_ds, all_ps, all_hs)
    delta_d = -alpha * 4*np.sum(all_w * (dm - all_ds) / all_r)
    delta_p = -alpha * np.sum(all_w * (pm - all_ps) / all_r)
    delta_h = -alpha * np.sum(all_w * (hm - all_hs) / all_r)

    return delta_d, delta_p, delta_h

def is_converge(delta_d, delta_p, delta_h, tol):
            """
            determine if ths system is converged or not
            """
            if abs(delta_d) < tol and abs(delta_p) < tol and abs(delta_h) < tol:
                return True
            
            return False


def gradient_descent(init_d, init_p, init_h, all_ds, all_ps, all_hs, all_w, alpha = 0.01, n_max = 10000, tol = 0.00001):

    dm, pm, hm = init_d, init_p, init_h

    for n in range(n_max):
         
        delta_d, delta_p, delta_h = get_delta(dm, pm, hm, all_ds, all_ps, all_hs, all_w, alpha)

        if is_converge(delta_d, delta_p, delta_h, tol):
            print("Converge after {} iteration steps".format(n))
            print("D, P, H of your material: ")
            print(dm, pm, hm)
            return dm, pm, hm, n
        
        dm += delta_d
        pm += delta_p
        hm += delta_h

    print("Warning: Reach maximum iterations. Fail to converge!")
    return dm, pm, hm, n
    


def calc_m(all_calc_vec, alpha = 0.01, n_max = 10000, tol = 0.00001):

    all_ds = np.array(all_calc_vec['all_ds'])
    all_ps = np.array(all_calc_vec['all_ps'])
    all_hs = np.array(all_calc_vec['all_hs'])
    all_w, all_w2 = get_weight(all_calc_vec['all_indicators'])

    init_d, init_p, init_h = init_guess(all_ds, all_ps, all_hs, all_w2)
    print('Initial guess of D, P, H: ')
    print(init_d, init_p, init_h)

    dm, pm, hm, n = gradient_descent(init_d, init_p, init_h, all_ds, all_ps, all_hs, all_w, alpha, n_max, tol)

    tm = calc_total_sp(dm, pm, hm)
    all_ts = calc_total_sp(all_ds, all_ps, all_hs)

    diff_ds, diff_ps, diff_hs, diff_ts = result_compare(dm, pm, hm, tm, all_ds, all_ps, all_hs, all_ts)

    result_r = get_distance(dm, pm, hm, all_ds, all_ps, all_hs)
    
    result_vec = all_calc_vec
    result_vec['all_ts'] = all_ts
    result_vec['dm'] = dm
    result_vec['pm'] = pm
    result_vec['hm'] = hm
    result_vec['tm'] = tm
    result_vec['e_d'] = diff_ds
    result_vec['e_p'] = diff_ps
    result_vec['e_h'] = diff_hs
    result_vec['e_t'] = diff_ts
    result_vec['R'] = result_r

    # print(result_vec)


    return result_vec

def calc_total_sp(d, p, h):
     
    t = np.sqrt(d**2 + p**2 + h**2)

    return t

def result_compare(dm, pm, hm, tm, ds, ps, hs, ts):

    diff_d = dm - ds
    diff_p = pm - ps
    diff_h = hm - hs
    diff_t = tm - ts

    return diff_d, diff_p, diff_h, diff_t










    






