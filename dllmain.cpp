//// dllmain.cpp : 定义 DLL 应用程序的入口点。
//#include "pch.h"
//#include <iostream>
//
//int Add(int a, int b)
//{
//	return a + b;
//}
//
//int Sub(int a, int b)
//{
//	return a - b;
//}



// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "pch.h"
#include <iostream>

_declspec(dllexport) int Add(int a, int b)
{
	return a + b;
}

_declspec(dllexport) int Sub(int a, int b)
{
	return a - b;
}
