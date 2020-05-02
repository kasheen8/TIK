# -*- coding: utf-8 -*-

from math import factorial as fact
import numpy as np
import sympy as sp


def prob_calc(n=1): #сокращение от probability calculation - функция для вычисления вероятностей при n повторных испытаний для построения вероятностной модели
    k = np.arange(0, n + 1, 1) #возможное число появлений события
    prob_list = {}
    p = sp.symbols('p')
    for test in k:
        Pn = fact(n) / (fact(test) * fact(n - test)) * np.power(p,test) * np.power(1 - p , n - test)
        prob_list[test] = Pn
    return prob_list

#def prob_calc_zero(n=1): #функция для вычисления вероятностей при n повторных испытаний, до первого появления события
    #k = np.arange(1,n+1,1) #количество событий
    #prob_list = {}
    #p = sp.symbols('p')
    #for test in k:
        #Pn = np.power(1-p,test)
        #prob_list[test] = Pn
    #return prob_list



def prob_calc_stand_part(n=5, m=2): #функция для вычисления вероятностей выбора стандартных деталей при выборе наугад m деталей, из партии n деталей, из которых k стандартных
    x = np.arange(0,m+1,1) #количество возможных отобранных стандарных деталей
    k = np.arange(0,n+1,1) #количество стандартных деталей
    full_prob_list = {}
    for num_part_standart in k:
        prob_list = {}
        for num_part_select in x:
            try:
                num_defect_part_select = m - num_part_select
                num_defect_part_standart = n - num_part_standart
                prob_standart = fact(num_part_standart) / (fact(num_part_select) * fact(num_part_standart - num_part_select))
                prob_defect = fact(num_defect_part_standart) / (fact(num_defect_part_select) * fact(num_defect_part_standart - num_defect_part_select))
                prob_all = fact(n) / (fact(m) * fact(n-m))
                Pm = (prob_standart * prob_defect) / prob_all
                prob_list[num_part_select] = Pm
            except ValueError:
                if num_part_select == num_part_standart == 0:
                    prob_list[num_part_select] = 1
                else:
                    prob_list[num_part_select] = 0
        full_prob_list[num_part_standart] = prob_list

    return full_prob_list


def formula_to_value_0_3(formula): #преобразование формулы в значение при p = 0,3 для отобржения в таблице
    p = sp.symbols('p')
    formula = formula.subs(p,0.3)
    formula = round(float(formula),5)
    return formula

def prob_calc_zero(propability):#функция для вычисления вероятности до первого появления события n
    sum_prob = 0
    k = 1
    prob_list = {}
    while sum_prob < 0.999:
        current_prob = (1 - propability)**(k-1) * propability
        sum_prob += current_prob
        prob_list[k] = round(current_prob,5)
        k += 1
    return prob_list





def formula_to_html(formula): #преобразование формулы в html-текст для отображения в таблице
    formula = str(formula)
    if formula.startswith('1.0*'):
        formula = formula[4:]
    formula = formula.replace('.0','')
    formula = formula.split('**')
    if len(formula) > 1:
        if len(formula) == 2:
            formula[0] = formula[0] + '<sup>'
            if formula[1].find('*') != -1:
                formula[1] = formula[1].replace('*','</sup>*')
            else:
                formula[1] = formula[1] + '</sup>'
        elif len(formula) == 3:
            formula[0] = formula[0] + '<sup>'
            formula[1] = formula[1].replace('*','</sup>*')
            formula[1] = formula[1] + '<sup>'
            formula[2] = formula[2] + '</sup>'
    formula = ''.join(formula)
    if formula.find(' 1*p') != -1:
        formula = formula.replace(' 1*p', ' p')
    formula = formula.replace('*','')
    formula = '<html><head/><body><p><b>' + formula + '</b></p></body></html>'
    return formula

def fucn_entropy(x_list,prob_list): #функция вычисления энтропии от значений p в 1 задаче
    p = sp.symbols('p')
    y = []
    for x in x_list:
        if x == 0 or x == 1:
            y.append(0)
            continue
        entropy = 0
        for k in prob_list.keys():
            entropy += -1 * prob_list[k].subs(p, x) * np.log2(float(prob_list[k].subs(p,x)))
        y.append(entropy)
    return y


def entropy_graph(prob_list): #функция возращает данные для графика энтропии в 1 задаче
    x = np.linspace(0,1,36)
    y = fucn_entropy(x,prob_list)
    return x,y

def func_entropy_zero(x_list):#функция вычисления энтропии от значений p в 2 задаче
    y = []
    for x in x_list:
        if x==0 or x==1:
            y.append(0)
            continue
        prob_list = prob_calc_zero(x)
        entropy = 0
        for k in prob_list.keys():
            entropy += -1 * prob_list[k] * np.log2(float(prob_list[k]))
        y.append(entropy)
    return y


def entropy_graph_zero(prob_list):#функция возращает данные для графика энтропии в 2 задаче
    x = np.linspace(0,1,36)
    y = func_entropy_zero(x)
    print(y)
    return x,y


def func_entropy_for_details(x_list, prob_list): #функция вычисления энтропии для каждого из возможных значений k
    y = []
    for k in x_list:
        entropy = 0
        for m in prob_list[k].keys():
            if prob_list[k][m] == 0:
                entropy += 0
            else:
                entropy += -1 * prob_list[k][m] * np.log2(prob_list[k][m])
        y.append(entropy)
    return y


def entropy_graph_for_details(prob_list): #функция возвращает данные для графика энтропии в 3 задаче
    x = np.linspace(0,len(prob_list)-1,len(prob_list))
    y = func_entropy_for_details(x,prob_list)
    return x,y



