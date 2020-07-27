package com.learn.kotlin.gradlespringboot
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class KotlinGradleSpringbootApplication

fun main(args: Array<String>) {
    runApplication<KotlinGradleSpringbootApplication>(*args)
}
