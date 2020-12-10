package com.learn.kotlin.utils

import kotlin.reflect.full.primaryConstructor

class ReflectGetPrivateFieldDemo (private val a:String="deufal",bb:String="AB"){

    private fun func() {

    }

    override fun toString(): String {
        return "ReflectGetPrivateFieldDemo(a='$a')"
    }


}
fun sum(x:Int,y:Int)=x+y //省略了{}

fun foo(n:Int):Int=if(n==0) 1 else n* foo(n-1) //需要显示生命返回类型


val sum={x:Int,y:Int->x+y}




fun main() {
//    for (i:Int in 1..11 step 2)print(i)
//    for(i in 1 until 10) print(i)

//    "a" in listOf("a","c")
    val a= ReflectGetPrivateFieldDemo("aaaaaaaa","aaaaaaaaaa")
    val b= ReflectGetPrivateFieldDemo("bbbbbbbbb","bbbbbbbbbbbbbb")::class.primaryConstructor
    println(b )

//   var data:ReflectGetPrivateFieldDemo= ReflectGetPrivateFieldDemo::class.java.getConstructor(String::class.java).newInstance("ssss")
//    print(data.javaClass.getField("a"))
//    print(data.javaClass.getDeclaredField("a").apply { isAccessible=true }.get(data))
}