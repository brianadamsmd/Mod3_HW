#!/usr/bin/env python
# coding: utf-8


print("Assignment 3\n\n")


"""QUESTION 1"""
print("Answer to Question 1\n")
##1a Create a list of integers no fewer than 10 items from 0 to 9.
one_a = list(range(10))
print(f"1.a: {one_a}")

##1b Add 3 to the 5th indexed element
##I assumed this meant to add 3 to whatever value was in the 5th indexed position.
one_a[5] += 3
print(f"1.b: {one_a}")

##1c Coerce all elements in the list to floats using list comprehension
one_c = [float(i) for i in one_a]
print(f"1.c: {one_c}")

##1d Coerce the list to a set
##I assumed that 1.c was temporary and I returned to using 1.a in this question for the remainder of this question.
one_d = set(one_a)
print(f"1.d: {one_d}")

##1e Using a method, append int 10 to the set
one_d.add(10)
print(f"1.e: {one_d}")

##1f Using a method, pop an item from the set
one_f = one_d.pop()
print(f"1.f: removed item: {one_f}: one_d: {one_d}")

##1g Using a length counting function, count the number of items in the set
one_g = len(one_d)
print(f"1.g: {one_g}")

##1h Check if the number of items in the set is the same as the number of items in the list
one_h = len(one_d) == len(one_a)
print(f"1.h: {one_h}")

##1i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
one_i = list(one_d) + one_a
print(f"1.i: {one_i}")

##1j Coerce 1.i to a set
one_j = set(one_i)
print(f"1.j: {one_j}")

##Ik Count the number of elements in the 1.j
one_k = len(one_j)
print(f"1.k: {one_k}")


"""QUESTION 2"""
print("\n\nAnswer to Question 2\n")

two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}
##2a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
        ##two_a, ensure the key names are the same as the dictionary names.
two_a = {"two_patient_dictionary_kinoko":{"name":"Kinoko","year":2021}, "two_patient_dictionary_dango":{"name":"Dango","year":2019}, "two_patient_dictionary_mochi":{"name":"Mochi","year":2020}}
print(f"2.a: {two_a}")

##2b Using keys, retrieve the Dango's name from 2.a
two_b = two_a["two_patient_dictionary_dango"]["name"]
print(f"2.b: {two_b}")

##2c Using keys, update the value of Mochi's year to 2018. This should not be a variable and should simply update 2.a.
two_a["two_patient_dictionary_mochi"]["year"] = 2018
print(f"2.c: {two_a}")

##2d Manually create a dictionary that has a single level and contains each patientas the key and the year as the value. Set Mochi's year to 2019.'
two_d = {"Kinoko":2021, "Dango":2019, "Mochi":2019}
print(f"2.d: {two_d}")

##2e Coerce the keys of 2.d into a list
two_e = list(two_d.keys())
print(f"2.e: {two_e}")

##2f Coerce the values of 2.d into a list
two_f = list(two_d.values())
print(f"2.f: {two_f}")

##2g Use the zip function to combine 2.e and 2.f into a dictionary again
two_g = dict(zip(two_e, two_f))
print(f"2.g: {two_g}")


"""QUESTION 3"""
print("\n\nAnswer to Question 3\n")

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

##3a Is set E a subset of set A
three_a = three_setE.issubset(three_setA)
print(f"3.a {three_a}: Is set E a subset of set A")

##3b Is set E a strict subset of set A
three_b = three_setE < three_setA
print(f"3.b {three_b}: Is set E a strict subset of set A")

##3c Create a set that is the intersection of set A and set B
three_c = three_setA.intersection(three_setB)
print(f"3.c The intersection of set A and set b is: {three_c}")

##3d Create a set that is the union of sets C, D and E
three_d = three_setC.union(three_setD, three_setE)
print(f"3.d The union of set C, D,and E is: {three_d}")

##3e add 9 to the set
three_d.add(9)
print(f"3.e 9 added to three_d: {three_d} - no change because this is a set")

##3f Using == compare this set to the list in one_a
three_f = three_d == one_a
print(f"3.f {three_f}: the set three_f == the list one_a.")

##3g Explain why they are not the same. What would you need to change if you wanted this to be True?
print("3.g: One variable would need to be cast to the other variable type. ie three_f would need be cast to a list using the list() method. Also a 0 would need to be added to the beginning to three_f.")


"""QUESTION 4"""
print("\n\nAnswer to Question 4\n")

## 4a Create a variable of type int with the value of 8
four_a = 8
print(f"4.a: {four_a}")

##4b Create an empty list
four_b = []
print(f"4.b: {four_b}")

##4c Using type(), add the type of 4.a to this list
four_b.append(type(four_a))
print(f"4.c: {four_b}")

##4d Add 0.39 to 4.c
four_b.append(0.39)
print(f"4.d: {four_b}")

##4e append the type of 0.39 to the list
four_b.append(type(0.39))
print(f"4.e: {four_b}")

##4f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an arithmetic operator to do so) round it to no decimal places, and append to list.
##I assumed the question asked to take the the 0.39 number addd to the the list in 4.d and raise it to the -10 (ie 0.39^-10)
four_b.append(round(four_b[1]**-10))
print(f"4.f: {four_b}")

##4g append the type to the list
four_b.append(type(round(four_b[1]**-10)))
print(f"4.g: {four_b}")


"""QUESTION 5"""
print("\n\nAnswer to Question 5\n")

##5a Manually create a dictionary where the values are items in the list from where we left in problem 4, and the keys should be their index in the list. Print the dictionary.
five_a = dict(enumerate(four_b))
print(f"5.a: {five_a}")

##5b Add 300 and coerce it into a string
##I continued using my list four_b where I had left off at the end for 4g. I continued to maipulate the list four_b for the rest of the assignment by just changing four_b to assign to new variables or to generate output.
four_b.append(str(300))
print(f"5.b: {four_b}")

##5c append the type to the list
four_b.append(type(four_b[5]))
print(f"5.c: {four_b}")

##5d slice the string up to the 2nd element
five_c = four_b[5][:2]
print(f"5.d: {five_c}")

##5e append the type to the list
four_b.append(type(four_b[5][:2]))
print(f"5.e: {four_b}")

##5f use list comprehension to convert this into a new list of integers
five_f = [int(item) for item in four_b if type(item) is not type]
print(f"5.f: {five_f}")

##5g append the type to the list
four_b.append(type(five_f))
print(f"5.g: {four_b}")

##5h append the type of three_setA to the list
four_b.append(type(three_setA))
print(f"5.h: {four_b}")

