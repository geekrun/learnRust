package com.learn.kotlin.reflect

/**
 * 255 -> 00 00 00 FF
 */

fun main() {
    print(123.toByte())
    val l=listOf(0.toByte(),1.toByte(),("-99").toByte()).toByteArray()
    print(l.toList())
}