package com.learn.kotlin.mavenspringboot

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class MavenSpringbootApplication

fun main(args: Array<String>) {
    runApplication<MavenSpringbootApplication>(*args)
}
