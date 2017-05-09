# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    

    s = get_session()
    client = s.create_client("cdn",region_name="cn-shanghai-2",use_ssl=False)

    ''' 
    get_cdn_domains 查询域名列表
        
    Parameters:
        PageSize        long    分页大小，默认20，最大500，取值1～500间整数 
        PageNumber      long    取第几页。默认为1，取值1～10000 
        DomainName      string  按域名过滤，默认为空，代表当前用户下所有域名 
        DomainStatus    string  按域名状态过滤，默认为空，代表当前用户下所有域名状态全部
        CdnType         string  产品类型，取值为download:下载类加速,live:直播加速，多个产品类型之间用逗号（半角）间隔，默认为空，代表当前用户下全部产品类型
        FuzzyMatch      string  域名过滤是否使用模糊匹配，取值为on：开启，off：关闭，默认为on
        
    Returns:
        <type 'dict'>
    '''  
    #res = client.get_cdn_domains(PageSize=20,PageNumber=0,DomainName='www.xunfei.cn',DomainStatus='online',CdnType='download')
 
       
    '''
    add_cdn_domain_request 新增域名
    
    Parameters:
        DomainName      string      需要接入CDN的域名
        CdnType         string      加速域名的产品类型 download:下载类加速,live:直播加速
        CdnSubType      string      加速业务子类型（业务子类型是为了细分业务，默认不填写）
        CdnProtocol     string      客户访问边缘节点的协议。默认http，直播必须填写：http＋flv， hls，rtmp
        BillingRegions  string      加速区域，默认CN， 可以输入多个，以逗号间隔
        OriginType      string      源站类型 取值：ipaddr、 domain、KS3、ksvideo分别表示：IP源站、域名源站、KS3为源站、金山云视频云源站
        OriginProtocol  string      回源协议，取值：http，rtmp，hls，https（当前版本不支持https回源)
        OriginPort      integer     可以指定 443, 80。默认值80。
        Origin          string      回源地址，可以是IP或域名；IP支持最多20个，以逗号区分，域名只能输入一个
        
    Returns:
        <type 'dict'>
    '''   
    #res = client.add_cdn_domain(DomainName='www.qidian.com',CdnType='download',CdnProtocol='http',OriginType='domain',OriginProtocol='http',Origin='www.ksyun.com')
      
      
    '''
    GetCdnDomainBasic 查询域名基础信息
    
    Parameters:
        DomainId    String      域名ID，只允许输入单个域名ID
        
    Returns:
        <type 'dict'>
    '''
    #domainBasic = client.get_cdn_domain_basic_info(DomainId='2D09NSH')
    
    
    '''
    GetDomainConfigs 查询域名详细配置信息
    
    Parameters:
        DomainId    String  域名ID
        ConfigList  String  需要查询的配置，多个配置用逗号（半角）分隔，不填代表查询所有 
                            当前支持  cache_expired、ip、error_page、http_header、optimize、page_compress、
                            ignore_query_string、range、referer、req_auth、src_host、video_seek、waf,notify_url, 
                            redirect_type 
        
    Returns:
    '''
    # res = client.get_domain_configs(DomainId='2D09NSH',ConfigList='cache_expired,ignore_query_string,src_host,referer,test_url,src_advanced')
    
    
    '''
    ModifyCdnDomainBasicInfo 修改域名基础配置
    
    Parameters:
        DomainId    String  域名ID
        Regions     String  加速区域，默认CN， 可以输入多个，以逗号间隔
        OriginType  String  源站类型 取值：ipaddr、 domain、KS3分别表示：IP源站、域名源站、KS3为源站。(此项目若输入，Origin必须输入)
        OriginPort  Integer 可以指定 443, 80。默认值80。443的话走https回源。当前版本只支持80.
        Origin      String  回源地址，可以是IP或域名；IP支持最多20个，以逗号区分，域名只能输入一个。IP与域名不能同时输入。 （此项目若输入，必须保证符合OriginType）
    Returns:
    '''
    #res = client.modify_cdn_domain_basic_info(DomainId='2D09NSH',Origin='',OriginType='',OriginPort='')
    
    
    '''
    StartStopCdnDomain  用于启用、停用某个加速域名
    
    Parameters:
        ActionType  String  操作接口名，系统规定参数 取值：start：启用；stop：停用；
        DomainId    String  需要启用或停用CDN服务的域名ID，只允许输入一个域名ID
        
    '''
    #res = client.start_stop_cdn_domain(DomainId='2D09NSH', ActionType='stop')
    
    
    '''
    DeleteCdnDomain  用于删除用户下已添加的加速域名  此操作只允许删除 DomainStatus 为已停止的域名；
    
    Parameters:
        DomainId    String  域名ID
    Returns:
        RequestID
    '''
    #res = client.delete_cdn_domain(DomainId='2D09NSH')
    
    
    '''
    SetIgnoreQueryStringConfig  设置过滤参数
    
    Parameters:
        DomainId    String  域名ID
        Enable      String  配置过滤参数功能的开启或关闭 取值：on、off ，默认为on
        
    '''
    #client.set_ignore_query_string_config(DomainId='2D09NSH', Enable='on')
    
    
    '''
    SetBackOriginHostConfig  设置回源host功能
                             注意： 若源站为KS3域名，需将ks3域名设置为回源host（即源站域名），方可正常回源
    Parameters:
        DomainId        String  域名ID
        BackOriginHost  String  是自定义回源域名，默认为空，表示不需要修改回源Host
    '''
    #client.set_back_origin_host_config(DomainId='2D09NSH', BackOriginHost='www.a.qunar.com')
    
    
    '''
    SetReferProtectionConfig  设置加速域名的Refer防盗链 加速域名创建后，默认不开启refer防盗链功能
    
    Parameters:
        DomainId    String  域名ID
        Enable      String  配置是否开启或关闭 取值：on、off，默认值为off关闭。开启时，下述必须项为必填项；关闭时，只更改此标识，忽略后面的项目。
        ReferType   String  refer类型，取值：block：黑名单；allow：白名单，开启后必填
        ReferList   String  逗号隔开的域名列表
        AllowEmpty  String  是否允许空refer访问,取值：on：允许；off：不允许；默认值：on。注：仅当选择白名单时，此项才生效
    '''
    #client.set_refer_protection_config(DomainId='2D09NSH', Enable='on', ReferType='block', ReferList='www.baidu.com,www.sina.com')

    '''
    SetIpProtectionConfig  设置加速域名的Ip防盗链 加速域名创建后，默认不开启Ip防盗链功能

    Parameters:
        DomainId    String  域名ID
        Enable      String  配置是否开启或关闭 取值：on、off，默认值为off关闭。开启时，下述必须项为必填项；关闭时，只更改此标识，忽略后面的项目。
        IpType      String  refer类型，取值：block：黑名单；allow：白名单，开启后必填
        IpList      String  逗号隔开的Ip列表
    '''
    # client.set_ip_protection_config(DomainId='2D09NN8', Enable='on', IpType='allow', IpList='1.1.1.1')

    '''
    SetCacheRuleConfig  设置缓存规则。加速域名创建后，默认缓存规则为空
                        更新加速域名的缓存规则为覆盖更新，需要对全部的规则进行修改，不能仅提交需要修改的部分
    Parameters:
        该接口需要输入json格式数据，并且在参数前面加上"**"
            DomainId    String      域名ID
            CacheRules  CacheRule[] 是由CacheRule组成的数组，表示缓存规则列表。注意：该数组是有序的
                CacheRule：
                    CacheRuleType   String  缓存规则类型 file_suffix 文件后缀 directory 目录 exact 全路径 url_regex 正则表达式
                    Value           String  缓存规则的内容，当缓存规则类型为目录时仅允许单条输入，目录必须以/开头且以/结尾；当缓存规则类型为全路径时仅允许单条输入，全路径需输入完整路径，且必须以/开头；
                                            当缓存规则类型为正则表达式时仅允许单条输入，且必须输入标准正则表达式；当缓存规则为文件后缀时允许多个输入，文件后缀必须输入英文文件后缀名，多个文件后缀名以逗号（半角）间隔
                    CacheTime       Long    缓存时间，以秒为单位
                    RespectOrigin   String  是否遵循源站，off表示不遵循，on（默认)表示遵循
                    IgnoreNoCache   String  是否忽略源站的no－cache头，on表示忽略，off（默认）表示不忽略。 (本期暂不支持此选项)
        
    '''
    
    ''' 
    # json格式规则
    cacheRules = {
            "DomainId":"2D09NSH",
            "CacheRules":
            [
                {
                "CacheRuleType":"directory",
                "Value":"/XXX/",
                "CacheTime":"11",
                "RespectOrigin":"",
                "IgnoreNoCache":""
                }
            ]
    }
    '''
    #client.set_cache_rule_config(**cacheRules)
    #confs = client.get_domain_configs(DomainId='2D09NSH', ConfigList='cache_expired,ignore_query_string,src_host,referer,test_url,src_advanced')
    
    
    '''
    SetTestUrlConfig  设置加速域名的测试URL
    
    Parameters:
        DomainId    String  域名ID
        TestUrl     String  测试URL列表，逗号间隔，默认为空
   
    '''
    #client.set_test_url_config(DomainId='2D09NSH', TestUrl='www.xinfei.cn/1.html')
    
    
    '''
    SetOriginAdvancedConfig   设置高级回源策略
                              OriginLine为default默认源的线路，是必填项，其他几个源都是选填项。OriginLine不能重复填写。开启高级回源策略后，会关闭掉基础配置中的回源配置                           
    Parameters:  
        该接口需要输入json格式数据，并且在参数前面加上"**"
            DomainId                String                  域名ID
            Enable                  String                  配置高级回源策略的开启或关闭 取值: on、off。注意：开启后会关闭掉基础配置中的的回源配置。默认值关闭。开启时，下述必须项为必填项；关闭时，只更改此标识，忽略后面的项目
            OriginType              String                  源站类型 取值：ipaddr、domain分别表示：IP源站、域名源站
            OriginAdvancedItems     OriginAdvancedItem[]    是由OriginAdvancedItem组成的数组，表示源站信息
            OriginPolicy            String                  rr: 轮询； quality: 按质量最优的topN来轮询回源
            OriginPolicyBestCount   Long                    当OriginPolicy是quality时，该项必填。取值1-10
            
                其中OriginAdvancedItem项的类型定义为
                        OriginLine  String  源站线路，取值: default：默认源； un： 联通源; ct: 电信源; cm: 移动源
                        Origin      String  回源地址，可以是IP或域名；IP支持最多20个，以逗号区分，域名只能输入一个。IP与域名不能同时输入。
    
    ''' 
    
    '''
    # json格式规则
    originParam = {
                    "DomainId":"2D09NSH",
                    "Enable":"on",
                    "OriginPort":80,
                    "OriginPolicy":"quality",
                    "OriginPolicyBestCount":1,
                    "OriginType":"domain",
                    "OriginAdvancedItems":[
                        {
                            "OriginLine":"default",
                            "Origin":"www.b.xunfei.cn"
                        },
                        {
                            "OriginLine":"cm",
                            "Origin":"www.c.xunfei.cn"
                        }
                    ]
                  }
    '''              
    #client.set_origin_advanced_config(**originParam)
    
    
    '''
    SetRemarkConfig    设置备注信息
    
    Parameters:
        DomainId    String  域名ID
        Remark      String  备注信息，默认为空
        
    '''
    #client.set_remark_config(DomainId='2D09NSH', Remark=u'备注信息')
    
    
    ####################以下为统计分析API###################
    
    '''
    GetBandwidthData    获取域名带宽数据，包括边缘带宽、回源带宽数据，单位：bit/second
            * 获取域名带宽数据，包括边缘带宽、回源带宽数据，单位：bit/second
            * 支持按指定的起止时间查询，两者需要同时指定
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔
            * 最多可获取最近一年内93天跨度的数据
            * 统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度的带宽值均取该粒度时间段的峰值
    
    Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        Regions         String  区域名称，缺省为 CN;  取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多区域查询，多个区域用逗号（半角）分隔
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        ResultType      String    取值为0：多域名多区域数据做合并；1：每个域名每个区域的数据分别返回
        Granularity     String    统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度；以上粒度的带宽值均取该粒度时间段的峰值
        DataType        String  数据类型， 取值为edge:边缘数据; origin:回源数据; 支持多类型选择，多个类型用逗号（半角）分隔，缺省为 edge
        
    '''
    #res = client.get_bandwidth_data(DomainIds='2D09VK5',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download',Granularity='240',ResultType='1',Regions='CN',DataType='origin')
    
    
    '''
    GetFlowData    获取域名流量数据，包括边缘流量、回源流量数据， 单位：byte
            * 获取域名流量数据，包括边缘流量、回源流量数据， 单位：byte
            * 支持按指定的起止时间查询，两者需要同时指定
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔
            * 最多可获取最近一年内93天跨度的数据
            * 统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度均取该粒度时间段的流量之和
    
    Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        Regions         String  区域名称，缺省为 CN;  取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多区域查询，多个区域用逗号（半角）分隔
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        ResultType      String    取值为0：多域名多区域数据做合并；1：每个域名每个区域的数据分别返回
        Granularity     String    统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度；以上粒度的带宽值均取该粒度时间段的峰值
        DataType        String  数据类型， 取值为edge:边缘数据; origin:回源数据; 支持多类型选择，多个类型用逗号（半角）分隔，缺省为 edge
        
    '''
    #res = client.get_flow_data(DomainIds='2D09VK5',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download',Granularity='240',ResultType='1',Regions='CN',DataType='origin')
    
    
    '''
    GetPvData       请求数查询  获取域名请求数数据，包括边缘请求数、回源请求数， 单位：次
            * 支持按指定的起止时间查询，两者需要同时指定
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔
            * 支持多区域查询，多个区域用逗号（半角）分隔
            * 最多可获取最近三年内93天跨度的数据
            * 统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度均取该粒度时间段的请求数之和
            *
            * 说明：
            * 请求数 ：统计当前域名下资源文件的访问次数
            
    Parameters:        
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        Regions         String  区域名称，缺省为 CN;  取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多区域查询，多个区域用逗号（半角）分隔
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        ResultType      String    取值为0：多域名多区域数据做合并；1：每个域名每个区域的数据分别返回
        Granularity     String    统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度；以上粒度的带宽值均取该粒度时间段的峰值
        DataType        String  数据类型， 取值为edge:边缘数据; origin:回源数据; 支持多类型选择，多个类型用逗号（半角）分隔，缺省为 edge
               
    '''
    #res = client.get_pv_data(DomainIds='2D09VK5',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download',Granularity='240',ResultType='0',Regions='CN',DataType='origin')
   
   
    '''
    GetHitRateDetailedData   命中率详情查询
            * 获取域名流量命中率、请求数命中率数据，单位：百分比
            * 支持按指定的起止时间查询，两者需要同时指定
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔
            * 最多可获取最近三年内93天跨度的数据
            * 统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；
            * 时效性：5分钟延迟
            
    Parameters: 
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速  
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        ResultType      String  取值为0：多域名多区域数据做合并；1：每个域名每个区域的数据分别返回
        Granularity     String  统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度；以上粒度的带宽值均取该粒度时间段的峰值
        HitType         String  数据类型， 取值为flowhitrate:流量命中率; reqhitrate:请求数命中率; 支持多类型选择，多个类型用逗号（半角）分隔，缺省为reqhitrate
        
    '''
    #res = client.get_hit_rate_detailed_data(DomainIds='2D09VK5',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download',Granularity='240',ResultType='0',HitType='flowhitrate')
    
    
    '''
    GetHitRateData  命中率查询（饼图），获取域名某一时间段内流量命中率、请求数命中率数据，用于绘制命中率饼图。
            * 获取域名某一时间段内流量命中率、请求数命中率数据
            * 支持按指定的起止时间查询，两者需要同时指定
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔
            * 最多可获取最近一年内93天跨度的数据
            * 说明
            * Hit访问次数=边缘请求数-回源请求数
            * Miss访问次数=回源请求数
            * Hit访问流量=边缘流量-回源流量
            * Miss访问流量=回源流量
            
    Parameters:    
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType     String  产品类型，只允许输入一种类型，取值为download:下载类加速,live:直播加速
        DomainIds   String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        
    '''
    #res = client.get_hit_rate_data(DomainIds='2D09VK5',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download')
    
    
    '''
    GetProvinceAndIspFlowData  省份+运营商流量查询，获取域名在中国大陆地区各省份及各运营商的流量数据，仅包括边缘节点数据，单位:byte
            * 支持按指定的起止时间查询，两者需要同时指定<p>
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔<p>
            * 最多可获取最近三年内93天跨度的数据<p>
            * 统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；**以上粒度均取该粒度时间段的流量之和**<p>
            * 使用场景<p>
            * 客户查询单个域名或多个域名在各个省份及运营商的合并后的实时流量数据<p>
            * 客户查询单个域名的详细流量数据，进行数据保存及数据分析<p>
            * 客户查询某一天或某1小时的详细流量区域分布，用于制作流量数据区域用量表<p>
            
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType     String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        DomainIds   String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        Provinces   String  省份区域名称， 取值详见枚举列表，支持多省份区域查询，多个省份区域用逗号（半角）分隔，缺省为全部省份区域
        Isps        String  运营商名称，取值详见枚举列表，支持多运营商查询，多个运营商用逗号（半角）分隔，缺省为全部运营商
        ResultType  String  取值为0：多域名多省份区域多运营商数据做合并；1：每个域名每个省份区域的每个运营商数据分别返回
        Granularity String  统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度
       
    '''
    #res = client.get_province_and_isp_flow_data(DomainIds='2D09VK5',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download',ResultType='1', Granularity='1440')
    
    
    '''
    GetProvinceAndIspBandwidthData   省份+运营商带宽查询 
            *获取域名在中国大陆地区各省市及各运营商的带宽数据，仅包括边缘节点数据，单位:bit/second
            * 支持按指定的起止时间查询，两者需要同时指定<p>
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔<p>
            * 最多可获取最近三年内93天跨度的数据<p>
            * 统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；**以上粒度均取该粒度时间段的流量之和**<p>
            * 使用场景<p>
            * 客户查询单个域名或多个域名在各个省份及运营商的合并后的实时流量数据<p>
            * 客户查询单个域名的详细流量数据，进行数据保存及数据分析<p>
            * 客户查询某一天或某1小时的详细流量区域分布，用于制作流量数据区域用量表<p>
            
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType     String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        DomainIds   String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        Provinces   String  省份区域名称， 取值详见枚举列表，支持多省份区域查询，多个省份区域用逗号（半角）分隔，缺省为全部省份区域
        Isps        String  运营商名称，取值详见枚举列表，支持多运营商查询，多个运营商用逗号（半角）分隔，缺省为全部运营商
        ResultType  String  取值为0：多域名多省份区域多运营商数据做合并；1：每个域名每个省份区域的每个运营商数据分别返回
        Granularity String  统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度
       
    '''
    #res = client.get_province_and_isp_bandwidth_data(DomainIds='2D09VK5',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download',ResultType='0', Granularity='1440')
    
    
    '''
    GetHttpCodeData    状态码统计(饼图)，获取域名一段时间内的Http状态码访问次数及占比数据,用于绘制饼图
            * 客户查询单个域名或多个域名一段时间内各状态码访问次数<p>
            * 支持按指定的起止时间查询，两者需要同时指定<p>
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔<p>
            * 最多可获取最近三年内93天跨度的数据<p>
            
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType     String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        DomainIds   String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
                
    '''
    #res = client.get_http_code_data(DomainIds='2D09NSH',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download')
    
    
    '''
    GetHttpCodeDetailedData    状态码详情统计，获取域名的Http状态码详细访问次数及占比数据
            * 客户查询单个域名或多个域名各状态码详细访问数据<p>
            * 支持按指定的起止时间查询，两者需要同时指定<p>
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔<p>
            * 最多可获取最近一年内93天跨度的数据<p>
            * 统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度，以上统计粒度均取该粒度内各状态码的访问次数之和<p>
    
    Parameters:    
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType     String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        DomainIds   String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        ResultType  String  取值为0：多域名多省份区域多运营商数据做合并；1：每个域名每个省份区域的每个运营商数据分别返回
        Granularity String  统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度     
        
    '''
    #res = client.get_http_code_detailed_data(DomainIds='2D09NSH',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download',ResultType='0')
    
    
    '''
    GetTopUrlData  top url 查询
            * 获取单个域名或多个域名某天内某一时段的TOP Url访问数据，仅包含Top200且访问次数大于15次的 Url的访问次数、访问流量，并按次数排序<p>
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔<p>
            * 最多可获取最近一年内一天跨度的数据<p>
            * 时效性：30分钟延迟<p>
            
    Parameters:        
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType     String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        DomainIds   String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        LimitN      String  热门Url条数，取值为1-200，最大200，默认100
    
    '''
    #res = client.get_top_url_data(DomainIds='2D09RW5',LimitN='100',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download')
    
    
    '''
    GetAreaData  用户区域统计
            * 获取国内各省份及运营商流量、访问次数、流量占比，请求数占比，海外地区的流量、访问次数、流量占比、请求数占比。<p>
            * 支持按指定的起止时间查询，两者需要同时指定<p>
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔<p>
            * 最多可获取最近一年内93天跨度的数据<p>
            * 说明<p>
            * 运营商包含：电信、联通、移动、铁通、鹏博士、教育网、其他、海外ISP<p>
            * 地区包含：国内32个省、香港、台湾、澳门、其他海外地区统一合并为海外<p>
            
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType     String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        DomainIds   String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        
    '''
    #res = client.get_area_data(DomainIds='2D09NSH',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download')
    
    
    '''
    GetIspData  运营商占比统计
            * 获取各运营商流量、访问次数、流量占比、访问次数占比<p>
            * 支持按指定的起止时间查询，两者需要同时指定<p>
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔<p>
            * 最多可获取最近一年内93天跨度的数据<p>
            * 说明
            * 运营商包含：电信、联通、移动、铁通、鹏博士、教育网、其他、海外ISP<p>
          
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType     String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        DomainIds   String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
            
    '''
    #res = client.get_isp_data(StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',CdnType='download')
    
    
    '''
    GetDomainRankingListData         域名排行查询
             * 获取用户维度下所有域名的流量、流量占比、带宽峰值、峰值时间、访问次数，并按流量排行
             * 单天维度，仅指定的单天时间查询
             * 支持批量域名查询，多个域名ID用逗号（半角）分隔
             * 最多可获取最近一年内以天为维度的数据
             * 注：仅展示查询日期内有效域名
             
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType     String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        
    '''
    #res = client.get_domain_ranking_list_data(StartTime='2016-11-20T08:00+0800',EndTime='2016-11-20T12:00+0800',CdnType='download')
    
    
    '''
    GetLiveFlowDataByStream    直播按流维度查询流量
            * 直播业务，获取按流为维度的流量数据<P>
            * 支持按指定的起止时间查询，两者需要同时指定<P>
            * 支持批量流名过滤查询，多个流名用逗号（半角）分隔<P>
            * 最多可获取最近62天内，7天跨度的数据<P>
            * 统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度均取该粒度时间段的求和<P>
            * 只支持直播业务<P>
            
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        StreamUrls   String  流名，支持批量查询，多个流名用逗号（半角）分隔
        Regions     String  计费区域名称，取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多计费区域查询，多个区域用逗号（半角）分隔，缺省为 CN
        ResultType  String  取值为0：多域名多省份区域多运营商数据做合并；1：每个域名每个省份区域的每个运营商数据分别返回
        Granularity String  统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度     
        
    '''
    #res = client.get_live_flow_data_by_stream(StartTime='2016-12-18T08:00+0800',EndTime='2016-12-20T08:00+0800',StreamUrls='rtmp://realflv3.plu.cn/live/ce781fecb2f6447d82d03590e520872f',ResultType='1',Regions='CN',Granularity='1440')
    
    
    '''
    GetLiveBandwidthDataByStream   直播按流维度查询带宽
            * 直播业务，获取按流为维度的带宽数据，带宽单位bit/second<p>
            * 支持按指定的起止时间查询，两者需要同时指定<p>
            * 支持批量流名过滤查询，多个流名用逗号（半角）分隔<p>
            * 最多可获取最近62天内，7天跨度的数据<p>
            * 统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度的带宽值均取该粒度时间段的峰值<p>
            * 只支持直播业务<p>
    
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        StreamUrls   String  流名，支持批量查询，多个流名用逗号（半角）分隔
        Regions     String  计费区域名称，取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多计费区域查询，多个区域用逗号（半角）分隔，缺省为 CN
        ResultType  String  取值为0：多域名多省份区域多运营商数据做合并；1：每个域名每个省份区域的每个运营商数据分别返回
        Granularity String  统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度     
        
    '''
    #res = client.get_live_bandwidth_data_by_stream(StartTime='2016-12-19T08:00+0800',EndTime='2016-12-20T08:00+0800',StreamUrls='rtmp://realflv3.plu.cn/live/ce781fecb2f6447d82d03590e520872f',ResultType='1',Regions='CN',Granularity='1440')
    
    
    '''
    GetLiveOnlineUserDataByDomain    直播按域名维度统计在线人数
            * 获取按域名维度的直播在线人数数据， 单位：每分钟的在线人数<p>
            * 支持按指定的起止时间查询，两者需要同时指定<p>
            * 支持批量域名查询，多个域名ID用逗号（半角）分隔<p>
            * 支持多计费区域查询，多个计费区域用逗号（半角）分隔<p>
            * 最多可获取最近1年93天跨度的数据<p>
            * 统计粒度：1分钟粒度（默认）；5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度均取该粒度时间段的在线人数的**峰值。<p>
            * 只支持直播业务<p>
            
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800       
        DomainIds   String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        Regions     String  计费区域名称，取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多计费区域查询，多个区域用逗号（半角）分隔，缺省为 CN
        ResultType  String  取值为0：多域名多省份区域多运营商数据做合并；1：每个域名每个省份区域的每个运营商数据分别返回
        Granularity String  统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度     
            
    '''
    #res = client.get_live_online_user_data_by_domain(DomainIds='2D09W0V',StartTime='2016-11-19T08:00+0800',EndTime='2016-11-20T08:00+0800',Regions='CN',Granularity='1440',ResultType='1')
    
    
    '''
    GetLiveOnlineUserDataByStream    直播按流维度统计在线人数
            * 获取按流维度的直播在线人数数据， 单位：每分钟的在线人数<p>
            * 支持按指定的起止时间查询，两者需要同时指定<p>
            * 支持批量流名过滤查询，多个流名用逗号（半角）分隔<p>
            * 支持多计费区域查询，多个计费区域用逗号（半角）分隔<p>
            * 最多可获取最近62天内，7天跨度的数据。（注意： 按流名维度的数据，只保留2个月）<p>
            * 统计粒度：1分钟粒度；5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度的在线人数均取该粒度时间段的在线人数的峰值 (注意： 需要按统计粒度来汇聚，用于在界面上展示。)<p>
            * 说明:<p>
            * 按流名维度的数据，返回时并不按照“域名”维度汇聚。如果需要按域名维度的数据，请按单个域名过滤<p>
            
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime     String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        StreamUrls   String  流名，支持批量查询，多个流名用逗号（半角）分隔
        Regions     String  计费区域名称，取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多计费区域查询，多个区域用逗号（半角）分隔，缺省为 CN
        ResultType  String  取值为0：多域名多省份区域多运营商数据做合并；1：每个域名每个省份区域的每个运营商数据分别返回
        Granularity String  统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度     
       
    '''
    #res = client.get_live_online_user_data_by_stream(StartTime='2016-12-19T08:00+0800',EndTime='2016-12-20T08:00+0800',StreamUrls='rtmp://realflv3.plu.cn/live/ce781fecb2f6447d82d03590e520872f',ResultType='0',Regions='CN',Granularity='5')
    
    
    '''
    GetLiveTopOnlineUserData    获取按流维度的直播在线人数排行， 单位：每分钟的在线人数<p>
            * 只设置起始时间，代表起始时间这1分钟的数据。<p>
            * 支持批量域名过滤查询，多个域名ID用逗号（半角）分隔<p>
            * 支持多计费区域查询，多个计费区域用逗号（半角）分隔<p>
            * 最多可获取最近62天内的数据。（注意： 按流维度的数据，只保留2个月）<p>
            * 说明：<p>
            * 按流名维度的数据，返回时并不按照“域名”维度汇聚。如果需要按域名维度的数据，请按单个域名过滤<p>
            
    Parameters:
        StartTime   String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        DomainIds   String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        Regions     String  计费区域名称，取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多计费区域查询，多个区域用逗号（半角）分隔，缺省为 CN
        ResultType  String  取值为0：多域名多省份区域多运营商数据做合并；1：每个域名每个省份区域的每个运营商数据分别返回
        LimitN 否 Int Top条数，取值为1-200，最大200，默认100
    '''
    #res = client.get_live_top_online_user_data(StartTime='2016-11-19T08:00+0800',ResultType='1',Regions='CN',LimitN='100')
    
    ''' 
    get_domain_logs 日志下载接口
        
    Parameters:
        PageSize        long    分页大小，默认20，最大500，取值1～500间整数 
        PageNumber      long    取第几页。默认为1，取值1～10000 
        DomainId      string  按域名过滤，默认为空，代表当前用户下所有域名 
        StartTime    string  查询开始时间，格式yyyy-MM-dd，开始时间和结束时间均不指定时，默认是当天
		EndTime    string  查询结束时间，格式yyyy-MM-dd，开始时间和结束时间均不指定时，默认是当天
    '''  
    #res = client.get_domain_logs(PageSize=20,PageNumber=1,DomainId='2D09X6F',StartTime='2017-01-01',EndTime='2017-02-23')
    
    
    #print '****************************cdn test*****************:'
    #print client.get_domain_configs(DomainId='2D09NSH', ConfigList='src_advanced')
    #print type(res)   
    #print res
    #print client.get_domain_configs(DomainId='2D09NSH', ConfigList='cache_expired,cc,page_compress,ignore_query_string,src_host,test_url,http_header,range,src_advanced')
    
    ''' 
    refresh_caches 刷新
        同一个 ID每日设有提交刷新类请求条数限制额度，与控制台共享此额度，具体额度可查看控制台或调用GetRefreshOrPreloadQuota接口获取
        刷新预热类接口包含 RefreshCaches刷新接口和PreloadCaches 预热接口
        Files与Dirs必须至少指定一种，可同时指定，即文件刷新和目录刷新可同时进行
		每个 Url 必须以http://或者https://开头
        每个 Url 最大长度 1000 字符
        每个 Url 所在的域名必须是该用户在金山云加速的域名。
        Url 如果包含中文字符
        单次调用 Url 上限为1000条
        预热仅支持Url，不支持目录预热，不支持正则
    Parameters:
        Files        Url[]    需要文件类型刷新的Url列表
        Dirs         Url[]    需要文件类型刷新的Url列表
        其中url[]为：
		Url String 需要提交刷新的Url，单条
    '''  
    '''
    # json格式规则
    param = {
              "Files": [
                 {
                   "Url": "http://test.dxz.ksyun.8686c.com/abc.txt"
                 },
                 {
                   "Url": "http://test.dxz.ksyun.8686c.com/test"
                 }],
              "Dirs": [
                 {
                   "Url": "http://test.dxz.ksyun.8686c.com/abc"
                 },
                 {
                   "Url": "http://test.dxz.ksyun.8686c.com/def"
                 }]
            }
    '''
    #res = client.refresh_caches(**param)
	
    ''' 
    preload_caches 预热
        同一个 ID 每日设有提交预热类请求条数限制额度，与控制台共享此额度，具体额度可查看控制台或调用GetRefreshOrPreloadQuota接口获取
        刷新预热类接口包含 RefreshCaches刷新接口和PreloadCaches 预热接口
		每个 Url 必须以http://或者https://开头
        每个 Url 最大长度 1000 字符
        每个 Url 所在的域名必须是该用户在金山云加速的域名。
        Url 如果包含中文字符
        单次调用 Url 上限为1000条
        预热仅支持Url，不支持目录预热，不支持正则
    Parameters:
        Urls         Url[]    需要文件类型预热的Url列表
        其中url[]为：
		Url String 需要提交预热的Url，单条
    '''  
    '''
    # json格式规则
    param = {
              "Urls": [
                 {
                   "Url": "http://test.dxz.ksyun.8686c.com/1.html"
                 }]
            }
    '''
    #res = client.preload_caches(**param)
    ''' 
    get_refresh_or_preload_task 预热进度查询
        本接口用于获取刷新、预热任务进度百分比及状态，查看任务是否在全网生效。
        支持根据任务ID、URL获取数据
        支持按指定的起止时间查询，两者需要同时指定
        所有参数都不指定，默认查7天内，第一页的数据（20条）
        起止时间、TaskId、Url可以同时指定，逻辑与的关系
        最多可获取7天内的数据
        使用场景：
           查询用户刷新或预热URL进度百分比及状态，查看是否在全网生效，用于在控制台展示
           客户通过API获取刷新或预热任务或URL进度百分比及状态，查看是否在全网生效
        注意：
           接口仅支持POST请求格式
    Parameters:
		PageSize        long    分页大小，默认20，最大500，取值1～500间整数 
        PageNumber      long    取第几页。默认为1，取值1～10000 
        StartTime    string  查询开始时间，格式yyyy-MM-dd，开始时间和结束时间均不指定时，默认是当天
		EndTime    string  查询结束时间，格式yyyy-MM-dd，开始时间和结束时间均不指定时，默认是当天
		TaskId    string   支持按任务ID查询，只允许输入单个任务ID
        Urls         Url[]    需要文件类型预热的Url列表
        其中url[]为：
		Url String 需要提交预热的Url，单条
    '''  
    '''
    # json格式规则
    param = {
           "StartTime":"2017-02-21T00:00+0800",
		   "EndTime":"2017-02-24T00:00+0800",
           "PageSize":10,
           "PageNumber":1,
		   "TaskId":"26ce0148-ef2e-4588-983c-c29077258020",
           "Urls":[
              {"Url": "http://test.dxz.ksyun.8686c.com/1.html"},
              {"Url": "http://test.dxz.ksyun.8686c.com/abc"}
             ]
           }
    '''
    #res = client.get_refresh_or_preload_task(**param)
    
    ''' 
    get_refresh_or_preload_quota 预热进度查询
        获取刷新、预热URL及目录的最大限制数量，及当日剩余刷新、预热URL及目录的条数
        刷新预热类接口包含 RefreshCaches刷新接口和PreloadCaches 预热接口
    '''  

    #res = client.get_refresh_or_preload_quota()
    ''' 
    set_domain_log_service 设置日志服务接口
        本接口用于启用、停用某个加速域名的日志服务。
		支持批量域名查询，多个域名ID用逗号（半角）分隔
		日志服务支持按域名维度启用、停用
		注意：域名对应账户如果由于欠费，或域名处于非法状态（审核中、审核失败、停用），则无法正常调用该接口启用加速域名的日志服务。
		     
    Parameters:
        ActionType      string  操作类型，取值为start：启用；stop：停用
        DomainIds    string  需要启用或停用日志服务的域名ID，支持批量域名开启或停用，多个域名ID用逗号（半角）分隔
		Granularity    Long  日志存储粒度，取值为60：按小时粒度存储；1440：按天粒度存储，当前暂不支持按小时粒度存储；开启时为必填，关闭时可不填
    ''' 
    #res = client.set_domain_log_service(ActionType="start",DomainIds="2D09SHE",Granularity=1440)
	
    ''' 
    get_domain_log_service_status 设置日志服务接口
        本接口用于获取域名日志服务状态。
		支持批量域名查询，多个域名ID用逗号（半角）分隔
		     
    Parameters:
        DomainIds    string  需要查询日志服务的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
    ''' 
    #res = client.get_domain_log_service_status(DomainIds="2D09SHE")
    
	
    '''
    GetUvData    获取域名独立请求的IP个数，单位：个
            支持按指定的起止时间查询，两者需要同时指定
            支持批量域名查询，多个域名ID用逗号（半角）分隔
            最多可获取最近一年内31天跨度的数据
            统计粒度：5分钟粒度
            时效性：30分钟延迟
            接口性能：接口最大吞吐量为10000，即DomainId个数*(EndTime-StartTime)\/统计粒度 <= 10000。注：在获取多个域名合并值时，DomainId个数按照1计算
            使用场景：
                        客户查询单个域名或多域名合并后独立请求IP的个数，用于绘制一条独立请求IP求数线图
                        客户查询单个域名的详细独立请求IP数据，进行数据保存及数据分析
            说明：
                        独立访问IP数：统计当前域名下独立请求的IP个数
    
    Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,live:直播加速，当前不支持直播类型
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        ResultType      Long    取值为0：多域名多区域数据做合并；1：每个域名每个区域的数据分别返回
        Granularity     Long     统计粒度，取值为 5（默认）：5分钟粒度；
    '''
    #res = client.get_uv_data(DomainIds='2D09QXN,2D09NRU',StartTime='2017-02-08T04:40+0800',EndTime='2017-02-08T07:26+0800',CdnType='download',Granularity=5,ResultType=1)
    '''
    GetTopReferData 获取域名某天内某一时段的热门页面访问数据排名，仅包含Top200且访问数大于15次的热门页面的访问次数、访问流量，并按次数排名
            支持批量域名查询，多个域名ID用逗号（半角）分隔
            最多可获取最近一年内24小时跨度的数据
            时效性：30分钟延迟
            使用场景：
                        查询单个域名或多个域名的热门来源Refer数据，进行热门页面数据分析
 
    Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,live:直播加速，当前不支持直播类型
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        LimitN     Long     热门Refer条数，取值为1-200，最大200，默认100
    '''
    #res = client.get_top_refer_data(DomainIds='2D09QJU',StartTime='2016-11-11T05:00+0800',EndTime='2016-11-11T05:05+0800',CdnType='download',LimitN=5)
    #res = client.get_uv_data(DomainIds='2D09QXN,2D09NRU',StartTime='2017-02-08T04:40+0800',EndTime='2017-02-08T07:26+0800',CdnType='download',Granularity=5,ResultType=1)
    '''
    GetTopIpData 
	本接口用于获取域名某天内某一时段的TOP IP访问数据，仅包含Top200且访问次数大于15次的独立请求的IP的访问次数、访问流量，并按次数排序
            支持批量域名查询，多个域名ID用逗号（半角）分隔
            最多可获取最近一年内24小时跨度的数据
            时效性：30分钟延迟
            使用场景：
                        查询单个域名或多个域名的独立请求的IP的访问数据，用于感知IP攻击
 
    Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,live:直播加速，当前不支持直播类型
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        LimitN     Long     热门Refer条数，取值为1-200，最大200，默认100
    '''
    #res = client.get_top_ip_data(DomainIds='2D09QJU',StartTime='2016-11-11T05:00+0800',EndTime='2016-11-11T05:05+0800',CdnType='download',LimitN=5)
    '''
    GetProvinceAndIspHitRateDetailedData 
	获取域名流量命中率、请求数命中率数据，单位：百分比
        支持按指定的起止时间查询，两者需要同时指定
        支持批量域名查询，多个域名ID用逗号（半角）分隔
        最多可获取最近一年内31天跨度的数据
        统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；
        时效性：5分钟延迟
        接口性能：接口最大吞吐量为10000，即Province个数*Isp个数*DomainId个数*(EndTime-StartTime)\/统计粒度 <= 10000。注：多域名多省份多运营商取合并数据时，Province个数、Isp个数、DomainId个数按照1计算。
        使用场景：
             客户查询单个域名或多域名在省份及运营商合并后实时命中率数据，用于绘制一条命中率线图
             客户查询单个域名的详细命中率数据，进行数据保存及数据分析
        说明：
			 请求数命中率=[边缘的hit状态的请求数\/边缘请求数]*100%
             流量命中率=[边缘的hit状态的流量\/边缘流量]*100%
             当边缘请求数或边缘流量为0时，命中率为0
			 
	Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,live:直播加速
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        Provinces     String     省份区域名称，取值详见枚举列表，支持多省份区域查询，多个省份区域用逗号（半角）分隔，缺省为全部省份区域
		Isps     String     运营商名称，取值详见枚举列表，支持多运营商查询，多个运营商用逗号（半角）分隔，缺省为全部运营商
		ResultType     Long     取值为0：多域名数据做合并；1：每个域名的数据分别返回
		Granularity     Long     热统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度；以上粒度均取该粒度时间段的流量之和、请求数之和
		HitType     String     数据类型， 取值为flowhitrate:流量命中率;reqhitrate:请求数命中率; 支持多类型选择，多个类型用逗号（半角）分隔，缺省为reqhitrate
    '''
    #res = client.get_province_and_isp_hit_rate_detailed_data(DomainIds='2D09SXW',StartTime='2017-02-08T10:00+0800',EndTime='2017-02-08T10:20+0800',CdnType='live',Provinces='liaoning',Isps='UN',ResultType=1,Granularity=5,HitType='reqhitrate,flowhitrate')
    
    '''
    GetProvinceAndIspHttpCodeData 
	获取域名一段时间内在中国大陆地区各省份及各运营商的Http状态码访问次数及占比数据（用于绘制饼图）
        支持按指定的起止时间查询，两者需要同时指定
        支持批量域名查询，多个域名ID用逗号（半角）分隔
        最多可获取最近一年内31天 跨度的数据
        时效性：5分钟延迟
        使用场景：
             客户查询单个域名或多个域名一段时间内在中国大陆地区各省份及各运营商的状态码访问次数，用于绘制状态码饼图

			 
	Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,live:直播加速，当前不支持直播类型
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        Provinces     String     省份区域名称，取值详见枚举列表，支持多省份区域查询，多个省份区域用逗号（半角）分隔，缺省为全部省份区域
		Isps     String     运营商名称，取值详见枚举列表，支持多运营商查询，多个运营商用逗号（半角）分隔，缺省为全部运营商
    '''
    #res = client.get_province_and_isp_http_code_data(DomainIds='2D09SXW',StartTime='2017-02-08T10:00+0800',EndTime='2017-02-08T10:20+0800',CdnType='download',Provinces='liaoning',Isps='UN')
    '''
    GetProvinceAndIspHttpCodeDetailedData 
        获取域名在中国大陆地区各省份及各运营商的Http状态码详细访问次数及占比数据（用于绘制状态码线图）
        支持按指定的起止时间查询，两者需要同时指定
        支持批量域名查询，多个域名ID用逗号（半角）分隔
        最多可获取最近一年内31天跨度的数据 统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度，以上统计粒度均取该粒度内各状态码的访问次数之和
        时效性：5分钟延迟
        接口性能：接口最大吞吐量为10000，即Province个数*Isp个数*DomainId个数*(EndTime-StartTime)\/统计粒度 <= 10000。注：多域名多省份多运营商取合并数据时，Province个数、Isp个数、DomainId个数按照1计算。
        使用场景：
            客户查询单个域名或多个域名在中国大陆地区各省份及各运营商的Http状态码详细访问数据，用于绘制状态码线图
            客户查询单个域名的详细状态码数据，进行数据保存及数据分析
	Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,live:直播加速，当前不支持直播类型
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        Provinces     String     省份区域名称，取值详见枚举列表，支持多省份区域查询，多个省份区域用逗号（半角）分隔，缺省为全部省份区域
		Isps     String     运营商名称，取值详见枚举列表，支持多运营商查询，多个运营商用逗号（半角）分隔，缺省为全部运营商
		Granularity     Long     统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度
		ResultType     Long     取值为0：多域名数据做合并；1：每个域名的数据分别返回
    '''
    #res = client.get_province_and_isp_http_code_detailed_data(DomainIds='2D09SXW',StartTime='2017-02-08T10:00+0800',EndTime='2017-02-08T10:20+0800',CdnType='download',Provinces='liaoning',Isps='UN',Granularity=5,ResultType=1)
	
    '''
    GetProvinceAndIspPvData 
        获取域名在中国大陆地区各省份及各运营商的请求数数据，包括边缘请求数， 单位：次
        支持按指定的起止时间查询，两者需要同时指定
        支持批量域名查询，多个域名ID用逗号（半角）分隔
        最多可获取最近一年内31天跨度的数据
        统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度均取该粒度时间段的请求数之和
        时效性：5分钟延迟
        接口性能：接口最大吞吐量为10000，即Province个数*Isp个数*DomainId个数*(EndTime-StartTime)\/统计粒度 <= 10000。
        注：在获取多个域名多个省份区域多个运营商合并值时，Province个数、Isp个数和DomainId个数按照1计算
        使用场景：
            客户查询单个域名或多个域名在各个省份及运营商的合并后的请求数数据，用于绘制一条请求数线图
            客户查询单个域名的详细请求数数据，进行数据保存及数据分析
        注意： 此处的请求数，仅包含边缘层的请求数。
	Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        Provinces     String     省份区域名称，取值详见枚举列表，支持多省份区域查询，多个省份区域用逗号（半角）分隔，缺省为全部省份区域
		Isps     String     运营商名称，取值详见枚举列表，支持多运营商查询，多个运营商用逗号（半角）分隔，缺省为全部运营商
		Granularity     Long     统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度
		ResultType     Long     取值为0：多域名数据做合并；1：每个域名的数据分别返回
    '''
    #res = client.get_province_and_isp_pv_data(DomainIds='2D09SXW',StartTime='2017-02-08T10:00+0800',EndTime='2017-02-08T10:20+0800',CdnType='download',Provinces='liaoning',Isps='UN',Granularity=5,ResultType=1)
    
    '''
    GetSrcHttpCodeData 
        获取域名一段时间内的回源Http状态码访问次数及占比数据（用于绘制饼图）
        支持按指定的起止时间查询，两者需要同时指定
        支持批量域名查询，多个域名ID用逗号（半角）分隔
        最多可获取最近一年内93天跨度的数据
        时效性：5分钟延迟
        使用场景：
            客户查询单个域名或多个域名一段时间内各回源状态码访问次数，用于绘制状态码饼图。
	Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        CdnType         String   产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速，当前暂不支持直播类型
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
    '''
    #res = client.get_src_http_code_data(DomainIds='2D09SXW',StartTime='2017-02-08T10:00+0800',EndTime='2017-02-08T10:20+0800',CdnType='download')
	
    '''
    GetSrcHttpCodeDetailedData 
        获取域名的回源Http状态码详细访问次数及占比数据（用于绘制状态码线图）
        支持按指定的起止时间查询，两者需要同时指定
        支持批量域名查询，多个域名ID用逗号（半角）分隔
        最多可获取最近一年内93天跨度的数据        统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度，以上统计粒度均取该粒度内各状态码的访问次数之和
        时效性：5分钟延迟
        使用场景：
                客户查询单个域名或多个域名回源状态码详细访问数据，用于绘制回源状态码线图
	Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        CdnType         String   产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速，当前暂不支持直播类型
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
		Granularity     Long     统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度
		ResultType     Long     取值为0：多域名数据做合并；1：每个域名的数据分别返回
	'''
    #res = client.get_src_http_code_detailed_data(DomainIds='2D09SXW',StartTime='2017-02-08T10:00+0800',EndTime='2017-02-08T10:20+0800',CdnType='download',Granularity=5,ResultType=1)
    
    '''
    GetBandwidthDataByDir 
        本接口用于获取某段时间内按一级目录为维度下消耗的带宽，单位bit\/second
        支持按指定的起止时间查询，两者需要同时指定
        仅支持下载域名查询
        仅支持单个域名查询
        支持批量目录过滤查询，多个目录用逗号（半角）分隔
        支持统计域名下一级目录所产生的带宽，即请求URL中域名后的第一个“\/”和第二个“\/”之间的内容
        当取不到一级目录时，即请求URL中域名后有且仅有一个“\/”时，将统计这部分请求URL产生的带宽并进行求和，以“\/”表示；
        最多可获取最近62天内24小时跨度的数据       统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度的带宽值均取该粒度时间段的峰值
        时效性：5分钟延迟
        接口性能：接口最大吞吐量为10000，即Region个数*Dir个数*(EndTime-StartTime)\/统计粒度 <= 10000。注：在获取多个目录多个区域合并值时，Dir个数和Region个数按照1计算
        使用场景：
        客户查询一个域名下单个或多个目录的带宽数据汇总，以单独查看或对比同一域名下不同目录的带宽曲线
        需配置白名单后方可调用此接口
    请求参数：
	Parameters:
        DomainId       String  输入需要查询的域名ID，只允许输入一个
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
		Granularity     Long     统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度
		ResultType     Long     取值为0：多域名数据做合并；1：每个域名的数据分别返回
		Regions       String  区域名称， 取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多区域查询，多个区域用逗号（半角）分隔，缺省为 CN
		Dirs       String  目录名称，支持统计域名下一级目录，即请求URL中域名后的第一个“\/”和第二个“\/”之间的内容;支持批量查询，多个目录用逗号（半角）分隔，缺省为该域名下所有一级目录及“\/”；若输入\/，则查询该域名下所有无一级目录的URL带宽合并值
	'''
    #res = client.get_bandwidth_data_by_dir(DomainId='2D09NMS',StartTime='2017-02-23T10:00+0800',EndTime='2017-02-23T10:21+0800',Dirs='',Granularity=5,ResultType=1,Regions='')
    '''
    GetFlowDataByDir 
        本接口用于获取某段时间内按一级目录为维度下消耗的流量，单位byte
        支持按指定的起止时间查询，两者需要同时指定
        仅支持下载域名查询
        仅支持单个域名查询
        支持批量目录过滤查询，多个目录用逗号（半角）分隔
        支持统计域名下一级目录所产生的带宽，即请求URL中域名后的第一个“\/”和第二个“\/”之间的内容
        当取不到一级目录时，即请求URL中域名后有且仅有一个“\/”时，将统计这部分请求URL产生的带宽并进行求和，以“\/”表示；
        最多可获取最近62天内24小时跨度的数据       统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度的带宽值均取该粒度时间段的峰值
        时效性：5分钟延迟
        接口性能：接口最大吞吐量为10000，即Region个数*Dir个数*(EndTime-StartTime)\/统计粒度 <= 10000。注：在获取多个目录多个区域合并值时，Dir个数和Region个数按照1计算
        使用场景：
        客户查询一个域名下单个或多个目录的带宽数据汇总，以单独查看或对比同一域名下不同目录的带宽曲线
        需配置白名单后方可调用此接口
    请求参数：
	Parameters:
        DomainId       String  输入需要查询的域名ID，只允许输入一个
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
		Granularity     Long     统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度
		ResultType     Long     取值为0：多域名数据做合并；1：每个域名的数据分别返回
		Regions       String  区域名称， 取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多区域查询，多个区域用逗号（半角）分隔，缺省为 CN
		Dirs       String  目录名称，支持统计域名下一级目录，即请求URL中域名后的第一个“\/”和第二个“\/”之间的内容;支持批量查询，多个目录用逗号（半角）分隔，缺省为该域名下所有一级目录及“\/”；若输入\/，则查询该域名下所有无一级目录的URL带宽合并值
	'''
    #res = client.get_flow_data_by_dir(DomainId='2D09NMS',StartTime='2017-02-23T10:00+0800',EndTime='2017-02-23T10:21+0800',Dirs='',Granularity=5,ResultType=0,Regions='')



    '''
    GetPlayTimeDataByStream
        本接口用于获取直播流维度的平均观看时长数据，单位：毫秒（ms）
        支持按指定的起止时间查询，两者需要同时指定
        支持批量流名查询，多个流名用逗号（半角）分割；多流名合并的方法为“将各流名的总播放时长，除以各流名的总访问次数”
        最大查询范围：最多可获取最近62天内，7天跨度的数据；
        统计粒度：5分钟粒度；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度的观看时长为该时段的播放时长总和，除以该时段的总访问次数
        时效性：5分钟延迟
        接口性能：接口最大吞吐量为10000，即Region个数*StreamUrl个数*(EndTime-StartTime)/统计粒度 <= 10000。注：在获取多个流名多个区域合并值时，Region个数和StreamUrl个数按照1计算
        使用场景：
           1）客户查询单个流名或多个流名，在一段时间内的合并后的平均观看时长，用于绘制一条曲线；
           2）客户查询单个流名或多个流名，在一段时间内的详细数据，用于画出多条曲线，表征每个流名的详细情况
        说明：只支持RTMP/HDL协议；

    请求参数：
	Parameters:
        StreamUrls      String  流名，支持批量查询，多个流名用逗号（半角）分隔
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
		Granularity     integer     统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度
		ResultType      integer     取值为0：多域名数据做合并；1：每个域名的数据分别返回
		Regions         String  区域名称， 取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多区域查询，多个区域用逗号（半角）分隔，缺省为 CN
	'''
    #res = client.get_play_time_data_by_stream(StreamUrls='http://c.gdown.baidu.com/live/m_defa5e0dd0d324101472363734966100.flv',StartTime='2017-04-23T10:00+0800',EndTime='2017-04-23T10:21+0800',Granularity=5,ResultType=1,Regions='')
    #print res

    '''
    GetPlayTimeDataByDomain
            本接口用于获取直播域名维度的观看时长数据，单位毫秒（ms）
            支持批量域名查询，批量域名合并的方法为“将各域名下各流名的总播放时长，除以各域名下各流名的总访问次数”；
            最大查询范围：最多可获取最近62天内，7天跨度的数据
            统计粒度：5分钟；10分钟粒度；20分钟粒度；1小时粒度；4小时粒度；8小时粒度；1天粒度；以上粒度的观看时长为该时段的播放时长总和，除以该时段的总访问次数；
            接口性能：接口最大吞吐量为10000，即Region个数*DomainId个数*(EndTime-StartTime)/统计粒度<= 10000。注：在获取多个域名多个区域合并值时，Region个数和DomainId个数按照1计算
            时效性：5分钟延迟；
            应用场景：
               1）客户查询单个域名或多个域名下的流名，在一段时间内的合并后的观看时长，用于绘制一条曲线；
               2）客户查询单个域名或多个域名下的流名，在一段时间内的详细数据，用于画出多条曲线，表征每个域名的详细情况
            说明：只支持RTMP/HDL协议；
    请求参数：
    Parameters:
        DomainIds       String  客户域名，支持批量查询，多个域名id用逗号（半角）分隔
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        Granularity     integer     统计粒度，取值为 5（默认）：5分钟粒度；10：10分钟粒度；20：20分钟粒度；60：1小时粒度；240：4小时粒度；480：8小时粒度；1440：1天粒度
        ResultType      integer     取值为0：多域名数据做合并；1：每个域名的数据分别返回
        Regions         String  区域名称， 取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多区域查询，多个区域用逗号（半角）分隔，缺省为 CN
    '''
    #res = client.get_play_time_data_by_domain(DomainIds='',StartTime='2017-04-23T10:00+0800',EndTime='2017-04-23T10:20+0800',Granularity=20,ResultType=1,Regions='')
    #print res



    '''
    GetBillingMode
        获取用户当前的计费方式。
        支持按产品类型查询
        使用场景：
           客户查询当前时刻用户维度下各产品类型的计费方式
    请求参数：
    Parameters:
        CdnType   String   产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
    '''
    #res = client.get_billing_mode(CdnType='live')
    #print res



    '''
    GetBillingData
        获取域名的计费数据
        支持按指定的起止时间查询，两者需要同时指定
        支持批量域名查询，多个域名ID用逗号（半角）分隔
        最多可获取最近一年内93天跨度的数据
        使用场景：
            客户查询域名计费数据，用于计费核算
            客户根据不同计费方式，对比不同计费数据值，用于计费方式调整依据。
        注意：
            1、95带宽峰值计费计算方法：，在选定时间段内，取每5分钟有效带宽值进行降序排列，然后把带宽数值前5%的点去掉，剩下的最高带宽就是95带宽峰值即计费值
            2、日峰值平均值带宽计算方法：在选定时间段内，取每一日的峰值带宽和，除以选择时间段的自然天数，得到一段时间内日峰值带宽的平均值即计费值
    请求参数：
    Parameters:
        DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        Regions         String  区域名称， 取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多区域查询，多个区域用逗号（半角）分隔，缺省为 CN
        BillingMode     String  计费方式， 取值为 peakbw:峰值计费;peak95bw:95峰值计费;averagebw：日峰值平均值计费；monthflow：流量按月，只允许输入一种计费方式，缺省为 peakbw ；
    '''
    #res = client.get_billing_data(StartTime='2017-02-01T00:00+0800',EndTime='2017-02-28T23:56+0800',CdnType='download',DomainIds='',BillingMode='monthflow',Regions='CN,AS,NA,AU')
    #print res
	
    '''
    GetServiceIpData
        获取域名当前的服务节点IP列表，用于分析域名服务节点运行状况，便于故障排查
        仅支持单个域名查询，配置黑白名单后才可生效
        使用场景：
            客户获取域名当前的服务节点IP，用于故障排查
          
    请求参数：
    Parameters:
        DomainId       String  域名ID，输入需要查询的域名ID，仅支持单个域名ID
    '''
    # res = client.get_service_ip_data(DomainId='2D09NK5')
    # print res

    '''
    GetPeakBandwidthData
        获取域名带宽峰值，峰值时间点
        1、峰值带宽计算方法：在选定时间段内，取每5分钟有效带宽值进行降序排列，最高带宽就是峰值带宽
        2、realtime，峰值时间点，取每5分钟一个时间点，最高峰出现的时间点即为峰值时间
        最多可获取最近一年内93天跨度的数据

    请求参数：
    Parameters:
         DomainIds       String  域名ID，缺省为当前产品类型下的全部域名，可输入需要查询的域名ID，支持批量域名查询，多个域名ID用逗号（半角）分隔
        StartTime       String  获取数据起始时间点，日期格式按ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如：2016-08-01T21:14+0800
        EndTime         String  结束时间需大于起始时间；获取日期格式按照ISO8601表示法，北京时间，格式为：YYYY-MM-DDThh:mm+0800，例如： 2016-08-01T21:14+0800
        CdnType         String  产品类型，只允许输入一种类型，取值为download:下载类加速,；live:直播加速
        Regions         String  区域名称， 取值为CN:中国大陆，HK：香港，TW：台湾，AS：亚洲其他，NA：北美洲，SA：南美洲，EU：欧洲，AU：大洋洲，AF：非洲，支持多区域查询，多个区域用逗号（半角）分隔，缺省为 CN
    '''
    res = client.get_peak_bandwidth_data(StartTime='2017-02-01T00:00+0800',EndTime='2017-02-28T23:56+0800',CdnType='download',Regions='CN,AS,NA,AU')
    print res