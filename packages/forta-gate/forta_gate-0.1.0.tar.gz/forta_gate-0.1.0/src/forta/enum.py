import enum

import pydantic_core


class RunMode(enum.StrEnum):
    dev = enum.auto()
    pro = enum.auto()


class OnecJsonNS(pydantic_core.Url, enum.ReprEnum):
    jxs = r'http://www.w3.org/2001/XMLSchema'
    jxsi = r'http://www.w3.org/2001/XMLSchema-instance'

    jstyle = r'http://v8.1c.ru/8.1/data/ui/style'
    jwin = r'http://v8.1c.ru/8.1/data/ui/colors/windows'
    jweb = r'http://v8.1c.ru/8.1/data/ui/colors/web'
    jsys = r'http://v8.1c.ru/8.1/data/ui/fonts/system'
    jcfg = r'http://v8.1c.ru/8.1/data/enterprise/current-config'
    jdcsdet = r'http://v8.1c.ru/8.1/data-composition-system/details'
    jdcscor = r'http://v8.1c.ru/8.1/data-composition-system/core'
    jdcsset = r'http://v8.1c.ru/8.1/data-composition-system/settings'
    jdcsapt = r'http://v8.1c.ru/8.1/data-composition-system/appearance-template'
    jdcsat = r'http://v8.1c.ru/8.1/data-composition-system/area-template'
    jdcscom = r'http://v8.1c.ru/8.1/data-composition-system/common'
    jdcsct = r'http://v8.1c.ru/8.1/data-composition-system/composition-template'
    jdcsres = r'http://v8.1c.ru/8.1/data-composition-system/result'
    jdcssch = r'http://v8.1c.ru/8.1/data-composition-system/schema'
    jent = r'http://v8.1c.ru/8.1/data/enterprise'
    jtxt = r'http://v8.1c.ru/8.1/data/txtedt'
    jv8 = r'http://v8.1c.ru/8.1/data/core'
    jv8ui = r'http://v8.1c.ru/8.1/data/ui'
    jxdm = r'http://v8.1c.ru/8.1/xdto'
    jwsm = r'http://v8.1c.ru/8.1/ws/wsdefinitions-model'

    jrole = r'http://v8.1c.ru/8.2/roles'
    jchm = r'http://v8.1c.ru/8.2/data/chart'
    japp = r'http://v8.1c.ru/8.2/managed-application/core'
    jcmi = r'http://v8.1c.ru/8.2/managed-application/cmi'
    jdl = r'http://v8.1c.ru/8.2/managed-application/dynamic-list'
    jlf = r'http://v8.1c.ru/8.2/managed-application/logform'
    jlfl = r'http://v8.1c.ru/8.2/managed-application/logform/layouter'
    jm = r'http://v8.1c.ru/8.2/managed-application/modules'
    jmng = r'http://v8.1c.ru/8.2/mngsrv/ws'
    jus = r'http://v8.1c.ru/8.2/managed-application/user-settings'
    juo = r'http://v8.1c.ru/8.2/uobjects'
    jda = r'http://v8.1c.ru/8.2/data/data-analysis'
    jgeo = r'http://v8.1c.ru/8.2/data/geo'
    jmxl = r'http://v8.1c.ru/8.2/data/spreadsheet'
    jsch = r'http://v8.1c.ru/8.2/data/graphscheme'
    jscript = r'http://v8.1c.ru/8.2/bsl'
    jvrs = r'http://v8.1c.ru/8.2/virtual-resource-system'
    jedbexc = r'http://v8.1c.ru/8.2/managed-application/edbexception'
    jscexc = r'http://v8.1c.ru/8.2/managed-application/seancecontextexception'
    jdeployment = r'http://v8.1c.ru/8.2/managed-application/deployment'
    jlfexc = r'http://v8.1c.ru/8.2/managed-application/logformexception'
    jbsch = r'http://v8.1c.ru/8.2/data/bsl'

    jxr = r'http://v8.1c.ru/8.3/xcf/readable'
    jxcf = r'http://v8.1c.ru/8.3/MDClasses'
    jxep = r'http://v8.1c.ru/8.3/xcf/extrnprops'
    jxpr = r'http://v8.1c.ru/8.3/xcf/predef'
    jxen = r'http://v8.1c.ru/8.3/xcf/enums'
    jxsch = r'http://v8.1c.ru/8.3/xcf/scheme'
    jextm = r'http://v8.1c.ru/8.3/data/ext'
