package com.learn.kotlin.utils

import java.lang.RuntimeException


fun parseItem(s: String): String {

    val item = s.split("_")
    val size = item.size
    val first_item = item.first()
    val name = captialStr(item.subList(1, size))
    when (first_item) {


        "str" -> {

            return "${name}: String ?= \"\","

        }
        "uint32" -> {

            return "${name}: Int ? = 0,"
        }
        "int32" -> {
            return "${name}: Int ? = 0,"
        }
        "rpt" -> {
            var new = captialStr(item.subList(2, size-1))
            if ("str".equals(item[1])){
                new="String"
            }
            return "${name}: List<${new.capitalize()}> = emptyList() ,"
        }
        "int64" -> {
            return "${name}: Long ? = 0L ,"
        }
        "uint64" -> {
            return "${name}: Long ? = 0L ,"
        }
        "bytes" -> {
            return "${name}: ByteArray ? = byteArrayOf() ,"
        }
        "msg" -> {
            return "${name}: ${name.capitalize()} ? = ${name.capitalize()}(),"
        }
        "msg11" -> {
            return "${name}: ${name.capitalize()}? = null ,"
        }
        "msg1" -> {
            return "${name}: ${name.capitalize()}?  ,"
        }
        "bool"->{
            return "${name}: Boolean =false,"
        }
    }

    return s

}


fun captialStr(items: List<String>, isDecap: Boolean = true): String {

    items.map { i -> i.capitalize() }.joinToString("").let {
        if (isDecap) {
            return it.decapitalize()
        } else {
            return it
        }
    }
}


fun covertProto(array: List<String>,indexs: List<String>,className:String="") {

    var result = mutableListOf<String>()
    array.forEachIndexed { index, s ->
        var indx=indexs.get(index).trim()
        try {
            var intIndx=indx.toInt().div(8)
            result.add("@ProtoId(${intIndx}) @JvmField val ${parseItem(s.trim())}")
        }catch (e:RuntimeException){
            result.add("@ProtoId(${indx}) @JvmField val ${parseItem(s.trim())}")
        }


    }
    result.let {

        it.add( it.removeLast().replace(",",""))
    }

    if (className.isNotEmpty()){
       println(
           """
@Serializable
internal class ApplyGetTrafficRsp(
${result.joinToString("\n")}
            ) : ProtoBuf
        
        
""")
    }else{
        println(result.joinToString("\n"))
    }

    println()



}


fun parseFiledName(raw:String):List<String>{
    val result = Regex("""new String\[\]\{(.*?)},""").find(raw)?.groups?.get(1)?.value

        if (result != null) {
            return result.replace("\"","").split(",")
        }

    println("解析字段名字错误")
    return listOf()
}

fun  paseeFiledIndex(raw: String):List<String> {
    val result = Regex("""new int\[\]\{(.*?)},""").find(raw)?.groups?.get(1)?.value

    if (result != null) {
       return result.replace("\"", "").split(",")

    }

        println("解析字段序号错误")
        return listOf()

    }



fun main() {
    var classNanme = "ApplyListDownloadRsp"
//    var a = arrayOf(
//            "uint32_cmd", "uint32_seq", "msg_recv_list_query_rsp", "msg_send_list_query_rsp", "msg_renew_file_rsp", "msg_recall_file_rsp", "msg_apply_upload_rsp", "msg_apply_upload_hit_rsp", "msg_apply_forward_file_rsp", "msg_upload_succ_rsp", "msg_delete_file_rsp", "msg_download_succ_rsp", "msg_apply_download_abs_rsp", "msg_apply_download_rsp", "msg_apply_list_download_rsp", "msg_file_query_rsp", "msg_apply_copy_from_rsp", "msg_apply_upload_rsp_v2", "msg_apply_upload_rsp_v3", "msg_apply_upload_hit_rsp_v2", "msg_apply_upload_hit_rsp_v3", "msg_apply_copy_to_rsp", "msg_apply_clean_traffic_rsp", "msg_apply_get_traffic_rsp", "msg_extension_rsp"
//    )
    var cc="""
        
         static final MessageMicro.FieldMap __fieldMap__ = MessageMicro.initFieldMap(new int[]{8, 16, 24, 34, 40, 48, 56, 64}, new String[]{"uint64_group_code", "uint32_app_id", "uint32_bus_id", "str_file_id", "bool_thumbnail_req", "uint32_url_type", "bool_preview_req", "uint32_src"}, new Object[]{0L, 0, 0, "", false, 0, false, 0}, DownloadFileReqBody.class);
        
    """.trimIndent()
    covertProto(parseFiledName(cc),paseeFiledIndex(cc))
}