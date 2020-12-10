package com.learn.kotlin.utils

/**
 * 返回手机号码
 */
private val telFirst = "134,135,136,137,138,139,150,151,152,157,158,159,130,131,132,155,156,133,153".split(",".toRegex())
private fun getTel(): String? {
    val index: Int = (telFirst.indices).random()
    val first: String = telFirst[index]
    val second: String = ((1..888).random() + 10000).toString().substring(1)
    val third: String = ((1..9100).random() + 10000).toString().substring(1)
    return first + second + third
}


fun main(){

    val qqId = 2104196423L//marvin
//    qqId = 1721199486//marvin 新注册
    var password = "jay19790118"//marvin的密码
    for (i in 1..100){
        println(getTel())
    }
}
