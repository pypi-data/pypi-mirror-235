'''# Third_party'''
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pywinauto
'''# built_in'''
import re
import os
import math
import importlib
from time import sleep
'''# custom'''
from common import PRIVATEDATA, GSDSTORE, MODULEDATA
from utils.public_Script import isLogicMethodClass
from utils.decorator import reset_implicitlyWait
from utils.log.trusteeship import trusteeship


'''Auxiliary Class 5'''
class Auxiliary:

    def __init__(self) -> None:
        return


    def element_index(self, locator_type, element, fun_type):
        '''返回指定位置函数在指定元素列表中的位置索引; 即：位置函数 >>> index索引'''
        '''注：该关键字需配合操作关键字【input_text、click_btn..】使用，单独使用无意义'''
        elems = self.locators(locator_type, element)
        index = 0  # 初始位置索引
        if fun_type == 'last':
            index = len(elems)-1  # 列表最后一个元素索引位置
        elif fun_type == 'center':
            index = math.floor(len(elems)/2)  # 列表“折中”元素索引位置
        return index


    def locator(self, locator_type, element):
        '''单元素定位'''
        element_object = None
        if locator_type == 'id':
            element_object = self.driver.find_element_by_id(element)
        elif locator_type == 'name':
            element_object = self.driver.find_element_by_name(element)
        elif locator_type == 'class_name':
            element_object = self.driver.find_element_by_class_name(element)
        elif locator_type == 'css_selector':
            element_object = self.driver.find_element_by_css_selector(element)
        elif locator_type == 'xpath':
            element_object = self.driver.find_element_by_xpath(element)
        elif locator_type == 'link_text':
            element_object = self.driver.find_element_by_link_text(element)
        elif locator_type == 'tag_name':
            element_object = self.driver.find_element_by_tag_name(element)
        '''返还定位结果'''
        return element_object


    def locators(self, locator_type, element, index=None):
        '''元素定位, 复数定位'''
        element_object = None
        if locator_type == 'ids':
            element_object = self.driver.find_elements_by_id(element)
        elif locator_type == 'names':
            element_object = self.driver.find_elements_by_name(element)
        elif locator_type == 'class_names':
            element_object = self.driver.find_elements_by_class_name(element)
        elif locator_type == 'css_selectors':
            element_object = self.driver.find_elements_by_css_selector(element)
        elif locator_type == 'xpaths':
            element_object = self.driver.find_elements_by_xpath(element)
        elif locator_type == 'link_texts':
            element_object = self.driver.find_elements_by_link_text(element)
        elif locator_type == 'tag_names':
            element_object = self.driver.find_elements_by_tag_name(element)
        '''返还定位结果'''
        try:
            return element_object[int(index)]
        except Exception as error:
            return element_object


    def offLocator(self, ParentObject, locator_type, element, index=None):
        '''后代元素定位'''
        element_object = None
        if locator_type[-1:] == 's':
            if locator_type == 'ids':
                element_object = ParentObject.find_elements_by_id(element)
            elif locator_type == 'names':
                element_object = ParentObject.find_elements_by_name(element)
            elif locator_type == 'class_names':
                element_object = ParentObject.find_elements_by_class_name(element)
            elif locator_type == 'css_selectors':
                element_object = ParentObject.find_elements_by_css_selector(element)
            elif locator_type == 'xpaths':
                element_object = ParentObject.find_elements_by_xpath(element)
            elif locator_type == 'link_texts':
                element_object = ParentObject.find_elements_by_link_text(element)
            elif locator_type == 'tag_names':
                element_object = ParentObject.find_elements_by_tag_name(element)
        else:
            if locator_type == 'id':
                element_object = ParentObject.find_element_by_id(element)
            elif locator_type == 'name':
                element_object = ParentObject.find_element_by_name(element)
            elif locator_type == 'class_name':
                element_object = ParentObject.find_element_by_class_name(element)
            elif locator_type == 'css_selector':
                element_object = ParentObject.find_element_by_css_selector(element)
            elif locator_type == 'xpath':
                element_object = ParentObject.find_element_by_xpath(element)
            elif locator_type == 'link_text':
                element_object = ParentObject.find_element_by_link_text(element)
            elif locator_type == 'tag_name':
                element_object = ParentObject.find_element_by_tag_name(element)
        '''返还定位结果'''
        try:
            return element_object[int(index)]
        except Exception as error:
            return element_object


    def location_ScreenOperation(self, targeting, element, index=None, ParentObject=None):
        '''元素筛选定位处理'''
        if ParentObject == None:
            if targeting[-1:] == 's':
                try:
                    ELEMENT = self.locators(targeting, element)[int(index)]
                except Exception:
                    # 无index值，默认为索引第一个
                    num = self.element_index(targeting, element, index) if index!=None else 0  # 使用位置函数
                    ELEMENT = self.locators(targeting, element)[num]
            else:
                ELEMENT = self.locator(targeting, element)
        else:
            ELEMENT = self.offLocator(ParentObject, targeting, element, index)
        return ELEMENT



'''37 pageAction'''
class KeyWordTest(Auxiliary):

    def __init__(self) -> None:
        self.driver = GSDSTORE['driver']
        '''文件 --> 缓存'''
        PRIVATEDATA['HANDLE'] = []  # 窗口句柄
        PRIVATEDATA['ELEVALUE'] = {}  # 元素缓存数据信息
        self.logicFunction_Object  = isLogicMethodClass()  # 实例化“公共逻辑处理方法”类对象


    def time_sleep(self, number):
        '''解释：设置强制时间等待'''
        sleep(int(number))


    def implicitly_time(self, number):
        '''解释：设置隐式时间等待'''
        self.driver.implicitly_wait(int(number))


    def explain(self, content):
        '''解释：该关键字无实际意义，只是起到说明作用'''
        trusteeship.info(f"keyword ---explain--- ：/***  {content}  ***/")


    def driver_back(self):
        '''解释：用于浏览器窗口返回上一页'''
        self.driver.back()


    def driver_refresh(self): 
        '''解释：用于浏览器窗口[刷新]'''
        self.driver.refresh()  


    def driver_close(self):
        '''解释：浏览器窗口关闭'''
        self.driver.close()
    

    def frame_default(self):
        '''解释：frame焦点初始化'''
        self.driver.switch_to.default_content()


    def parent_frame(self):
        '''解释：frame焦点切换到上层(iframe嵌套时使用)'''
        self.driver.switch_to.parent_frame()


    def refresh_frame(self):
        '''解释：刷新当前iframe页面'''
        self.driver.execute_script("window.location.reload(true);")


    def switch_frame(self, element):
        '''解释：frame跳转'''
        try:
            element = int(element)  # 对传入数据进行值判断，int转换
        except Exception as error:
            self.driver.switch_to.frame(element)
        else:
            self.driver.switch_to.frame(element)
    

    def Interface_Invoke(self, YAML_PATH):
        '''解释：调用公共接口类 Common_Interface_Class'''
        _Interface = importlib.import_module('Interface.common_Interface_Class')  # 动态导入common_Interface_Class模块
        _object = _Interface.CommonInterfaceClass()
        if not _object(YAML_PATH): 
            trusteeship.info(f"keyword ---Interface_Invoke--- ：/***  用例步骤接口执行结果: {False}  ***/")
            raise Exception
        else:
            trusteeship.info(f"keyword ---Interface_Invoke--- ：/***  用例步骤接口执行结果: {True}  ***/")
    

    def ternary_Judgement(self, targeting=None, element=None, index=None, content=None):
        '''解释：三元判断，支持对指定元素的属性、文本值以及单独的条件表达式进行处理，已达到控制用例步骤执行的目的'''
        '''
            content: list 类型；列表第一项为判断条件，第二项为关键字控制行数。[条件list/string, 控制行数int]
             判断条件：可接受两种类型参数 list、string
                list：在对元素的属性、文本值做判断时传入该类型； [[属性名,]关系运算符,预期值]，属性名可省略
                string：表示单独条件表达式；例如 A==B、C>=D

             控制行数：int类型；代表在关键字条件成立的情况下所控制的步骤行数
             
            注意：
             1、不论判断条件采用何种形式书写，可选用的关系运算符为 ==、>=、<=、!=、>、<、in、not in，其它的运算符无法识别
             2、在判断条件采用“单独条件表达式”形式时，支持在表达式中使用逻辑运算符 and、or、not
             3、在判断条件采用“单独条件表达式”形式时，元素定位相关的数据无论书写与否均不会生效
             4、在判断条件采用“元素判断”形式时，元素定位参数为必填项，为空则关键字无法正常执行
             5、在判断条件采用“元素判断”形式时，元素属性值若省略则代表对元素的text文本值做判断
             6、在判断条件采用“元素判断”形式时，关键字的条件判断依据为“实际结果”；例如 “实际结果 >= 预期结果”、“实际结果 包含 预期结果”
             7、在判断条件采用“元素判断”形式时，若所指定的“属性名”在元素中不存在，则将其直接转化在“预期结果”中
             8、在判断条件采用“元素判断”形式时，若所指定的“关系运算符”不合法，则将其直接转化在“预期结果”中
             9、关键字所控制的单元行从当前行向下覆盖，不包括当前行。例如 “当前行为3，若控制行数为2，则控制 4、5两行”
             10、不论判断条件采用何种形式书写，若条件不成立则关键字作废，所控制的单元行自动释放
        '''
        effectCondition, effectRow = eval(content)
        if isinstance(effectCondition, list):
            '''元素判断'''
            attribute, operator, expect = [None, None, None]
            ELEMENT = self.location_ScreenOperation(targeting, element, index)

            for item in effectCondition:
                if ELEMENT.get_attribute(item):attribute = item; continue  # 属性
                if re.findall('^>=$|^<=$|^==$|^!=$|^>$|^<$|^in$|^not in$', item):operator = item; continue  # 关系运算符
            else:
                if attribute: effectCondition.remove(attribute)
                if operator: effectCondition.remove(operator)
                expect = ''.join(map(str, effectCondition))  # 预期结果
            
            if operator in ['in', 'not in']:
                if not(eval(f"'{expect}' {operator} '{ELEMENT.get_attribute(attribute) if attribute else ELEMENT.text}'")): effectRow = 0
            else:
                if not(eval(f"'{ELEMENT.get_attribute(attribute) if attribute else ELEMENT.text}' {operator} '{expect}'")): effectRow = 0
            trusteeship.info(f"keyword ---ternary_Judgement--- ：/***  三元判断-元素判断: {bool(effectRow)}  ***/")
        else:
            '''条件表达式'''
            if not(eval(effectCondition)): effectRow = 0
            trusteeship.info(f"keyword ---ternary_Judgement--- ：/***  三元判断-表达式判断: {bool(effectRow)}  ***/")

        return f"isCycleSS_{abs(effectRow)}"


    def input_text(self, targeting, element, index=None, content=None, ParentObject=None):
        '''解释：内容输入操作；如果想要在输入时清空对应的输入框，则content应为list类型：['XX']、[XX]'''
        ELEMENT = self.location_ScreenOperation(targeting, element, index, ParentObject)
        try:
            if isinstance(eval(content), list):
                content = eval(content)
            else:
                raise Exception
        except Exception as error:
            ELEMENT.send_keys(content)
        else:
            ELEMENT.clear()
            if content: ELEMENT.send_keys(str(content[0]))


    def click_btn(self, targeting, element, index=None, ParentObject=None):
        '''解释：按钮点击操作'''
        ELEMENT = self.location_ScreenOperation(targeting, element, index, ParentObject)
        try:
            ELEMENT.click()  # 直接进行点击操作
        except Exception as error:
            self.driver.execute_script("arguments[0].click();", ELEMENT)  # 穿透元素点击，解决点击捕获和遮挡问题


    def js_control(self, targeting, element, behavior, index=None, content=None):
        '''解释：使用指定的 “javaScript定位操作表达式” 对目标元素进行操作'''
        JS_REG = None
        try:
            '''输入'''
            if content == None: raise Exception
            JS_REG = f'{targeting}("{element}")[{index}].{behavior}="{content}"' if (index != None) else f'{targeting}("{element}").{behavior}="{content}"'
        except Exception as error:
            '''无输入'''
            JS_REG = f'{targeting}("{element}")[{index}].{behavior}' if (index != None) else f'{targeting}("{element}").{behavior}'
        finally:
            self.driver.execute_script(JS_REG)
        
    
    def alert_operation(self, content=None):
        '''解释：对alert提示弹框进行操作'''
        '''
         content 参数支持接收三种类型的参数值，关键字会根据参数值的类型进行相应的处理
            None: 代表点击 `alert`、`confirm`和 `prompt`弹框的“取消”按钮
            string: 代表在 `prompt`弹框的输入框中输入的文本
            boole: 代表点击 `alert`、`confirm`和 `prompt`弹框的那个操作按钮（True确定、False取消）
            list: 上面两种类型数据的整合，[string, boole]; 代表对`prompt`弹框进行输入，并点击弹框的指定操作按钮
        
         注：
            1、关键字的弹框操作按钮类型默认为`Fasel取消`，即若不传入，则在处理弹框时将默认点击弹框的【取消】按钮。
            2、参数值为string类型时，弹框类型必须为`prompt`，否则会出现异常报错。
            3、在参数值为list类型时，列表子项必须由 string、boole两项组成，缺一不可；另外两项没有顺序限制，[string, boole] 和 [boole, string] 均可。
            4、在处理 `prompt`弹框时建议参数类型为list类型，若单独传入“boole 点击操作按钮”或者“string 输入框文本输入”均无实际意义。
        '''
        isOperType = False; isPromptText = None
        try:
            thisAlertObject = WebDriverWait(self.driver, 2, 0.5).until(EC.alert_is_present())
            try:
                if isinstance(eval(content), list):
                    '''list [...]'''
                    isOperType = [value for value in eval(content) if isinstance(value, bool)][0]
                    isPromptText = [value for value in eval(content) if isinstance(value, str)][0]
                else:
                    raise Exception
            except Exception as error:
                '''None/true/false/text'''
                try:
                    if isinstance(eval(content), bool): isOperType = eval(content)
                    else: raise Exception
                except:
                    isPromptText = content
            finally:
                if isPromptText: thisAlertObject.send_keys(isPromptText)
                thisAlertObject.accept() if isOperType else thisAlertObject.dismiss()
        except:
            trusteeship.info(f"keyword ---alert_opertaion--- ：/*** 未检测到alert弹框，或关键字传值错误！！ ***/")


    def selector_operation(self, targeting, element, index=None, content=None, ParentObject=None):
        '''解释：对指定的<select>元素进行列表项选择操作，可根据列表项的[value属性值、index索引值、text文本值]对其进行选择'''
        '''
         说明: 
            1、content形参为list类型，支持接收[value属性值、index索引值、text文本值]中的任意一个。
            2、关键字会根据实际的情况对传入值的类型进行判断，不需要特殊声明。
            3、content接收的列表中仅允许存在一个元素，若存在多个元素则以索引位置为0的元素为准。
        '''
        ELEMENT = Select(self.location_ScreenOperation(targeting, element, index, ParentObject))
        content = eval(content)
        try:
            content = "".join(content) if not (len(content) - 1) else "".join([content[0]])
        except Exception as error:
            '''index'''
            ELEMENT.select_by_index(content[0])  # index
        else:
            '''string'''
            if content in [item.text for item in ELEMENT.options]:
                ELEMENT.select_by_visible_text(content)  # text
            else:
                ELEMENT.select_by_value(content)  # value
    

    def radioCheck_operation(self, targeting, element, index=None, content=None, ParentObject=None):
        '''解释：对指定的“单/复选按钮”元素进行选中操作，可自动识别当前元素状态(是否选中)决定是否继续操作'''
        '''
         content：代表元素选中操作标识；True[默认]对元素进行选中，False指定元素不选中
         注：若元素的状态(是否选中)与元素选中标识(content)不一致则对元素进行操作，若一致则忽略跳过。
        '''
        try:
            if isinstance(eval(content), bool):
                content = eval(content)
            else:
                raise Exception
        except:
            content = True
        finally:
            ELEMENT = self.location_ScreenOperation(targeting, element, index, ParentObject)
            if ELEMENT.is_selected() != content: self.driver.execute_script("arguments[0].click();", ELEMENT) # 操作


    def drag_scrollBar(self, targeting, element, index=None, content=None, ParentObject=None):
        '''解释：用于对窗口滚动条的拖动；以达到被遮挡元素显示的目的'''
        '''
         content：代表在拖动滚动条后目标元素的窗口对齐位置；top[默认]与窗口顶部对齐，bottom与窗口低部对齐
        '''
        place = {None: 'true', 'top': 'true', 'bottom': 'false'}
        ELEMENT = self.location_ScreenOperation(targeting, element, index, ParentObject)
        self.driver.execute_script(f"arguments[0].scrollIntoView({place[content]});", ELEMENT)  # 拖动到可见的元素


    def title_assert(self, content):
        '''解释：用于窗口、页面title标题值断言判断；【content代表预期比对结果,如果需要包含值比较书写为“[xxx]”】'''
        try:
            if isinstance(eval(content), list):
                content = str(eval(content)[0])
            else:
                raise Exception
        except Exception as error:
            trusteeship.info(f"keyword ---title_assert--- ：/***  相等值比较: {self.driver.title}    预期: {content}  ***/")
            return True if self.driver.title == str(content) else False
        else:
            trusteeship.info(f"keyword ---title_assert--- ：/***  包含值比较: {self.driver.title}    预期: {content}  ***/")
            return True if self.logicFunction_Object.mutual_in(self.driver.title, content) else False
    
    
    def alert_assert(self, content):
        '''解释：对alert提示框文本进行断言；如果需要进行包含值比较，则值需要包裹在“[]”中'''
        try:
            thisAlertObject = WebDriverWait(self.driver, 2, 0.5).until(EC.alert_is_present())
            try:
                if isinstance(eval(content), list):
                    trusteeship.info(f"keyword ---alert_assert--- ：/***  包含值比较: {thisAlertObject.text}    预期: {eval(content)[0]}  ***/")
                    return self.logicFunction_Object.mutual_in(thisAlertObject.text, eval(content)[0])
                else:
                    raise Exception
            except Exception as error:
                trusteeship.info(f"keyword ---alert_assert--- ：/***  相等值比较: {thisAlertObject.text}    预期: {content}  ***/")
                return thisAlertObject.text == content
        except:
            trusteeship.info(f"keyword ---alert_assert--- ：/*** 未检测到alert弹框***/"); return False


    def selector_assert(self, targeting, element, index=None, content=None, ParentObject=None):
        '''解释：用于对<select>标签列表子项进行检查，验证预期列表项是否存在或者当前选中的列表项是否为预期列表项''' 
        '''
            content传参说明：
             1、'预期值' ：代表要验证<select>下拉列表框当前选中的“子项文本值”是否与“预期预期列表值”一致。
             2、('预期值',) ：代表要验证“预期列表值”是否包含在<select>下拉列表框的子项中(预期列表项是否存在与<select>下拉列表框的子项中)。

            注：
             1、如果想要进行值“包含”比较，则需要将要比较的预期值包裹在中括号[]中；例如：['预期值']   (['预期值'],)
             2、关键字中所有有关列表项的“值断言”均采用列表项的text文本值，不支持对value值和index值做断言；
             3、注意在进行“预期列表项是否存在”断言时，要注意参数中的 ,号为python语法不可省略；('预期值',)  (['预期值'],)
        '''
        ELEMENT = self.location_ScreenOperation(targeting, element, index, ParentObject)
        select_object = Select(ELEMENT); actual_result = None; expect_result = None; assert_type = False
        try:
            '''值包含在下拉列表框的子项中'''
            content = eval(content)
            if isinstance(content, tuple):
                assert_type = True
                actual_result = [item.text.strip() for item in select_object.options]
                expect_result = next(iter(content))
            else:
                raise Exception
    
        except Exception as error:
            '''当前选中值'''
            actual_result = select_object.first_selected_option.text.strip()
            expect_result = content
        
        finally:
            if isinstance(expect_result, list):
                trusteeship.info(f"keyword ---selector_assert--- ：/*** {'子项包含' if assert_type else '当前值'} -- 包含值比较: {actual_result}    预期: {expect_result[0]}  ***/")
                if assert_type:
                    '''值包含在下拉列表框的子项中'''
                    return True if [item for item in actual_result if (self.logicFunction_Object.mutual_in(expect_result[0], item))] else False
                else:
                    '''当前选中值'''
                    return True if self.logicFunction_Object.mutual_in(actual_result, expect_result[0]) else False
            else:
                trusteeship.info(f"keyword ---selector_assert--- ：/*** {'子项包含' if assert_type else '当前值'} -- 相等值比较: {actual_result}    预期: {expect_result}  ***/")
                if assert_type:
                    '''值包含在下拉列表框的子项中'''
                    return True if expect_result in actual_result else False
                else:
                    '''当前选中值'''
                    return True if actual_result == expect_result else False


    @reset_implicitlyWait(1)
    def elementNumber_assert(self, targeting, element, content, ParentObject=None):
        '''解释：返回指定定位元素的个数，并与传入的预期结果数值进行比较'''
        '''
         注：
            1、该关键字中采用复数定位的方法，不对单元素定位进行操作；
            2、如果 content[比对值]中出现多个数字，则默认取获取到的第一个数字；例如：“测试12测试34” [处理后] “12”
            3、如果想要使用python表达式来计算预期结果，则将你的表达式包含在“[]”中，传给关键字；例如 [int('2') - (int('1')-1)*10]
            4、若传入的为python表达式，则关键字不会进行“条目2”中所述的筛选；
        '''
        try:
            if isinstance(eval(content), list):
                C_content = int(eval(content)[0])
            else:
                raise Exception
        except Exception as error:
            C_content = int(self.logicFunction_Object.Regular_takeData(content, 'int')[0]) if isinstance(content, str) else int(content)
        finally:
            if ParentObject == None:  # 一级元素
                number = self.locators(targeting, element)
            else:  # 后代元素
                number = self.offLocator(ParentObject, targeting, element)
        trusteeship.info(f"keyword ---elementNumber_assert--- ：/***  实际元素个数：{len(number)}    预期比对个数：{C_content}  ***/")
        return True if len(number) == C_content else False
        

    def elementErgodic_assert(self, targeting, element, content):
        '''解释：适用于完成一个操作之后，对界面的元素的某项值进行遍历比较 - 预期值存在'''
        '''
         # content：list类型
          列表第一项为要进行比较的预期结果值
          列表第二项为要获取元素的那个属性值，如value/class...,如果省略则默认为text； 例如：['123','src'] / ['123']
          列表第三项为布尔值，代表取反逻辑标识 [True正常逻辑 默认]；例如：['123','src',True] / ['123',False]
          True正常逻辑，即当前实际结果中有任意一条记录与预期结果不相等，则return False; 如果所有记录全部相符则return True
          False取反逻辑，即当前实际结果中有任意一条记录与预期结果相等，则return True; 如果没有一条记录相符则return False

         注：
            a、该关键字中采用复数定位方法，不对单元素进行操作
            b、如果想要对预期结果进行值“包含”比较，则需要将要比较的预期结果表达为list类型/[]；例如：[['123'],'src'] 或者 [[0],'class']
        '''
        result = []  # 判定结果暂存
        expect = eval(content)
        expect_Value = "".join(expect[0]) if isinstance(expect[0], list) else expect[0]
        Reverse_Switch = expect[-1] if isinstance(expect[-1], bool) else True  # 关键字断言逻辑

        eles = self.locators(targeting, element)  # 获取要操作的元素
        for ele in eles:
            actual_Value = ele.get_attribute(expect[-1]) if (len(expect) == 2 and isinstance(expect[-1], str))\
                else ele.get_attribute(expect[1]) if len(expect) == 3 else ele.text
            trusteeship.info(f"keyword ---elementErgodic_assert--- ：/***  预期: {expect_Value}    实际: {actual_Value.strip()}  ***/")

            result.append(
                True if actual_Value.strip() == expect_Value else True if isinstance(expect[0], list) and\
                    self.logicFunction_Object.mutual_in(actual_Value.strip(), expect_Value) else False
            )
            trusteeship.info(f"keyword ---elementErgodic_assert--- : /***  判定: {result}  ***/")

            if Reverse_Switch:
                '''正常'''
                if False in result: return False
            else:
                '''取反'''
                if True in result: return True
        # 未在循环中跳出
        return (True if Reverse_Switch else False) if eles else False
    
    
    def elementErgodicNot_assert(self, targeting, element, content):
        '''解释：适用于完成一个操作之后，对界面的元素的某项值进行遍历比较 - 预期值不存在'''
        '''
         # content：list类型
          列表第一项为要进行比较的预期结果值
          列表第二项为要获取元素的那个属性值，如value/class...,如果省略则默认为text； 例如：['123','src'] / ['123']

         注：
            a、该关键字中采用复数定位方法，不对单元素进行操作
            b、如果想要对预期结果进行值“包含”比较，则需要将要比较的预期结果表达为list类型/[]；例如：[['123'],'src'] 或者 [[0],'class']
        '''
        content = eval(content)
        expect_Value = "".join(content[0]) if isinstance(content[0], list) else content[0]

        eles = self.locators(targeting, element)  # 获取要操作的元素
        for ele in eles:
            actual_Value = ele.get_attribute(content[-1]).strip() if len(content) == 2 else ele.text.strip()
            trusteeship.info(f"keyword ---elementErgodicNot_assert--- ：/***  预期: {expect_Value}    实际: {actual_Value}  ***/")

            result = (
                False if actual_Value == expect_Value else False if isinstance(content[0], list) and self.logicFunction_Object.mutual_in(actual_Value, expect_Value) else True
            )
            trusteeship.info(f"keyword ---elementErgodicNot_assert--- : /***  判定: {result}  ***/")
            if not result: return False

        return True  # 未在循环中跳出


    @reset_implicitlyWait(1)
    def elementExistence_assert(self, targeting, element, index=None, content=None, ParentObject=None):
        '''解释：用于判断指定的元素是否存在(指定元素是否存在于DOM树中并可见), 元素可见并且元素的高和宽都大于0'''
        '''
         # content：boolean类型；代表关键字的判定依据[True：指定元素预期存在、False(默认)：指定元素预期不存在]
        '''
        try:
            content = eval(content)
        except Exception as error:
            content = False
        finally:
            try:
                ELEMENT = self.location_ScreenOperation(targeting, element, index, ParentObject)
                WebDriverWait(self.driver, 1, 0.5).until(EC.visibility_of(ELEMENT))
            except Exception as error:
                '''false'''
                return (True if not content else False)
            else:
                '''true'''
                return (True if content else False)


    def elementComparison_assert(self, targeting, element, index=None, content=None):
        '''解释：用于对元素值的大小进行比较，支持对 “单个元素” 和 “复数元素” 进行[<, >, >=, <=, ==]关系运算。'''
        '''
         说明: 
            1、content形参可接收 “string” 和 “list” 两种类型的参数，代表要进行操作的表达式。
            2、关键字同时支持对 “单个元素” 和 “复数元素” 进行操作，关键字会根据实际传入的“定位表达式”进行判断，无需特殊指明。

         注：对content参数进行重点解释：
            1、当传入的content参数为 “string” 类型时，表示要进行比较的预期结果；关键字将默认以 “>大于” 对预期结果和实际结果进行比较。
            2、当传入的content参数为 “list” 类型时，['预期结果', '关系运算符', ['属性名']]，表示要对某个预期进行进行某种关系的比较。
             (列表首项代表“预期结果”，第二项代表要关键字进行何种“关系运算”，第三项则代表要关键字对实际元素的何种“属性值”比较[可省略]); 
            3、“list列表” 两种合法传值举例: ['预期结果', '关系运算符']  ||  ['预期结果', '关系运算符', '属性名']
            4、传入的 “list列表” 各索引位置不可变动，若无'属性名'项，则关键字默认取元素的'文本'。
            5、无论是进行那种关系运行，关键字的比较值均为“实际结果”；例如 “实际结果 > 预期结果”、“实际结果 < 预期结果”...
        '''
        relationship_Runner = None  # 关系运算符
        expect_Element_Value = None  # 预期结果
        expect_Element_Attribute = None  # 预期属性
        actual_Result_List = []  # 判定结果列表
        try:
            if isinstance(eval(content), list):
                content = eval(content)
            else:
                raise Exception
        except Exception as error:
            '''string'''
            relationship_Runner = '>'
            expect_Element_Value = str(content)
        else:
            '''list'''
            try: content[2]
            except: pass
            else: expect_Element_Attribute = content[2]
            finally:
                relationship_Runner = content[1]
                expect_Element_Value = str(content[0])

        elements_Array = self.locators(targeting, element, index)
        mathematical_Expression = f"element.get_attribute('{expect_Element_Attribute}').strip()" if expect_Element_Attribute else "element.text.strip()"
        for element in elements_Array:
            trusteeship.info(f"keyword ---elementComparison_assert--- : /***  实际: {eval(mathematical_Expression)}  {relationship_Runner}  预期: {expect_Element_Value}***/")
            actual_Result_List.append(
                True if eval(f"{mathematical_Expression} occupy expect_Element_Value".replace('occupy', relationship_Runner)) else False
            )
        return True if not (False in actual_Result_List) else False


    def selfText_assert(self, targeting, element, index=None, content=None):
        '''解释：获取元素的text文本值进行断言判断'''
        '''
         注：
            1、如果想要对预期结果进行包含值比较，则content应为list类型，例如：['XX']；如果不需要预期结果包含比较，则直接原样传入预期结果即可。
            2、该关键字只支持对string类型的数据进行“包含值比较”，其它类型的数据会自动判别为“相等值比较”，例如：传入[1]，关键字会认为是对数字1与实际结果做相等值比较。
            3、不必担心你在Excel步骤文件中传入的值是否为string类型，关键字会进行自动转换，例如：传入数字5关键字会自动转换成'5'。
            4、传入""代表为空
        '''
        textValue = self.location_ScreenOperation(targeting, element, index).text.strip()
        try:
            if isinstance(eval(content), list):
                content = str(eval(content)[0])
            else:
                raise Exception
        except Exception as error:
            trusteeship.info(f"keyword ---selfText_assert--- : /***  相等值比较: {textValue}    预期: {content}  ***/")
            return (not len(textValue)) if content == '""' else (textValue == str(content))
        else:
            trusteeship.info(f"keyword ---selfText_assert--- : /***  包含值比较: {textValue}    预期: {content}  ***/")
            return self.logicFunction_Object.mutual_in(textValue, content)


    def selfAttribute_assert(self, targeting, element, index=None, content=None):
        '''解释：获取元素的指定属性进行断言判断'''
        '''
         # content为列表，第一个元素代表属性，第二个元素代表预期结果，第三个元素代表是否对实际属性结果进行截取；例如：['src','test2.jpeg',True]
        '''
        '''
         注：
            a、列表第三个元素为boole类型；如果为True则代表根据预期结果对实际属性结果进行截取，False代表原样
                例如：实际结果：XXXXXXX001.gif, 预期结果：002.gif, 则根据预期结果的长度对实际结果进行截取为001.gif
            b、如果想要对预期结果进行值“包含”比较，则需要将要比较的预期结果表达为list类型/[]
                例如：['src',['123']] 或者 ['src',[0]]
            c、要进行比较的预期结果只能为一个值，不可进行多值比较；且在实际调用时“实际结果预处理”与“值包含比较”可同时使用
        '''
        content = eval(content)
        intercept = content[2] if len(content)-2 else None  # 实际结果预处理判断
        expect_Result = "".join(content[1])  # 预期结果值提取

        tran_Attribute = self.location_ScreenOperation(targeting, element, index).get_attribute(content[0]).strip()
        '''[::-1]：代表倒序'''
        attribute = tran_Attribute[-1:-(len(expect_Result)+1):-1][::-1] if intercept else tran_Attribute
        trusteeship.info(f"keyword ---selfAttribute_assert--- : /***  预期结果: {expect_Result}    实际结果: {attribute}  ***/")
        '''进行值比较'''
        return self.logicFunction_Object.mutual_in(attribute, expect_Result) if isinstance(content[1],list) else attribute == expect_Result


    def functionReturn_assert(self, content):
        '''解释：按照需求调用指定的插件方法，并对插件方法的返回结果进行断言判断'''
        '''
         content：为list列表类型，存放三个值
            第一个值为要进行比较的预期结果。
            第二个值为要进行调用的插件方法名，按照“[插件名]方法名”的方式书写。
            第三个值为插件方法的参数列表，支持采用list(顺序传递)和dict(指定参数)两种方式传参；若无需参数时该项可省略不写。

         例如(content)：
            ['预计比对结果文本','[插件名]方法名',['1','2','3']]  # 插件方法带参调用，并按照list(顺序传递)方式将参数传递给插件方法。
            ['预计比对结果文本','[插件名]方法名',{'参数1':'1', '参数3':'3', '参数2':'2'}]  # 插件方法带参调用，并按照dict(指定参数)方式将参数传递给插件方法。
            ['预计比对结果文本','[插件名]方法名']  # 插件方法无参调用
        '''
        splitValue = eval(content)  # 数据拆分处理
        returnResult = None  # 插件方法返回结果
        pluginName = "".join(re.findall(r'[[](.*?)[]]', splitValue[1])); functionName = splitValue[1][splitValue[1].find(']') + 1:]
        fun_Object = getattr(MODULEDATA[pluginName]['object'], functionName)
        try:
            splitValue[2]
        except Exception as error:
            '''无参'''
            returnResult = fun_Object()
        else:
            '''带参'''
            if isinstance(splitValue[2], dict):
                returnResult = fun_Object(**splitValue[2])  # 指定
            else:
                returnResult = fun_Object(*splitValue[2])  # 顺序
        trusteeship.info(f"keyword ---functionReturn_assert--- ：/***  插件方法返回值: {returnResult}    预期: {splitValue[0]}  ***/")
        return splitValue[0] == returnResult


    def downloadExport_assert(self, prospectiveControl):
        '''解释：对下载或者导出的项(文件)进行断言判断'''
        '''
         # prospectiveControl: string类型，预期对照值(文件名)；若需要进行包含值比较则该值书写为['预期对照内容']。
        '''
        result_dir = GSDSTORE["WORKPATH"]["downloadPath"]  # 导出检查目录
        file_List = os.listdir(result_dir)
        file_List.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn)); file = os.path.join(result_dir, file_List[-1])
        name = re.sub(r'\(.*?\)', "", file_List[-1]).strip(); result_name = re.sub(r'\s+', '', name).strip()

        if '未确认' in result_name:
            '''安全警示，文件大小检查'''
            file_size = os.path.getsize(f'{result_dir}\\{name}')
            trusteeship.info(f"keyword ---downloadExport_assert--- : /***  安全警示检查文件大小: {file_size}  ***/")
            return bool(int(file_size))
        else:
            '''文件名判断'''
            trusteeship.info(f"keyword ---downloadExport_assert--- : /***  实际比对值: {result_name}    预期对照值: {prospectiveControl}  ***/")
            return self.__logicFunction_Object.mutual_in(result_name, "".join(prospectiveControl))\
                if isinstance(prospectiveControl, list) else\
                    result_name == prospectiveControl


    def winUpload(self, filePath):
        '''解释：处理页面非<input type="file">标签(窗口批量上传)的文件上传，支持同一目录/不同目录下的多文件上传；目前只针对windows操作系统'''
        '''
         # filePath: list类型，列表子项为要上传文件的绝对路径。
        '''
        fileQueue = " ".join([f'"{file}"' for file in eval(filePath)])
        windowObject = pywinauto.Desktop()
        selfWindow = windowObject['打开']
        selfWindow["Toolbar3"].click()
        selfWindow["文件名(&N):Edit"].type_keys(fileQueue)  # 文件名输入
        selfWindow["打开(&O)"].click_input()


    def actionBuilder_Move(self, targeting, element, index=None, ParentObject=None):
        '''解释：鼠标悬停'''
        ELEMENT = self.location_ScreenOperation(targeting, element, index, ParentObject)
        ActionChains(self.driver).move_to_element(ELEMENT).perform()


    def actionBuilder_RightClick(self, targeting, element, index=None, ParentObject=None):
        '''解释：鼠标右键点击'''
        ELEMENT = self.location_ScreenOperation(targeting, element, index, ParentObject)
        ActionChains(self.driver).context_click(ELEMENT).perform()


    def actionBuilder_DoubleClick(self, targeting, element, index=None, ParentObject=None):
        '''解释：鼠标双击操作'''
        ELEMENT = self.location_ScreenOperation(targeting, element, index, ParentObject)
        ActionChains(self.driver).double_click(ELEMENT).perform()
    

    def keyBoard_Events(self, targeting, element, index=None, content=None, ParentObject=None):
        '''解释：键盘事件'''
        ELEMENT = self.location_ScreenOperation(targeting, element, index, ParentObject)
        '''如果为退格键操作则关键字会自动根据操作元素中的文字数量进行相应次数的事件执行'''
        '''目前该操作只兼容输入框和多行文本输入框'''
        frequency = len(ELEMENT.get_attribute('value')) if content == "Keys.BACK_SPACE" else 1
        for i in range(0, frequency): ELEMENT.send_keys(eval(content))


    def getElementText(self, targeting, element, index=None, content=None):
        '''解释：未知属性值比较第一步，获取元素值'''
        '''
         说明：
            · 适用于删除等界面元素比较操作 【可指定属性获取】。
            · content : 代表要获取取元素值的操作表达式；可接收三种类型的数据 None/string/List。

         注：对content参数进行重点解释：
            1、当参数值为空(None)时：代表要对元素的text文本值进行随机保存；随机保存时的key键为“key_当前时间戳”。
            2、当参数值为string类型时：关键字可以接收三种操作值中的任意一个“key键/ attribute何种属性/ condition筛选出何种类型的数据”，并根据传入的操作值对目标元素进行处理。
            3、当参数值为list类型时：可以同时接收三种操作值 [key键, attribute何种属性, condition筛选出何种类型的数据]进行处理，并根据传入的操作值对目标元素进行处理。

         注：关键字使用规则解释：
            1、当content参数值为list类型时，其中各项可随意书写不需要按照特定顺序书写，关键字会自动进行判别筛选; 例如[key, attribute, condition] || [attribute, condition , key]。
            2、不管content为何种参数形式，只要是出现“未指定key键”的情况，关键字则默认以“key_当前时间戳”为key键将获取到的值存入到数据文件中。
            3、如果出现 “指定属性名不存在”的情况，则该“不存在”的属性名将视情况而定自动转为key键。
             · 关键字未指定key键: 例如'value(属性不存在)'则key键名为：value
             · 关键字已指定key键: 例如 ['key_One(这里表示key键)', 'value(属性不存在)'] 则key键名为：key_Onevalue
            4、如果出现“获取属性重复”的情况，则“权重低”的属性名将视情况而定自动转为key键。
             · 关键字未指定key键: 例如 ['value'(判定为属性),'onclick'(判定为key键)]。
             · 关键字已指定key键: 例如 ['key_One(这里表示key键)', 'value(表示属性，判定为属性)', 'onclick(表示属性，判定为key键)'] 则key键名为：key_Oneonclick
            5、如果出现 “key键” 与 “attribute何种属性”同名情况时，权重最高的值判定为属性顺位为key键; 例如['value'(判定为属性),'value'(判定为key键)]。
            6、关键字中支持5种数据类型的筛选，为['int 整型', 'text'文本字符串, 'date 日期', 'time 时间', 'dateTime 日期时间']，注意传入时各项均为string类型。
            7、如果出现“关键字筛选结果不唯一”的情况，则筛选结果列表中的第一项为筛选的最终结果。
             · 12VALUE14: 使用“int”筛选标识，将目标数据中的所有“整型数字”筛选出来的结果为 “12”
             · 汉123字: 使用“text”筛选标识，将目标数据中所有“汉字文本”筛选出来的结果为 “汉”
        '''
        element_Obtained = self.location_ScreenOperation(targeting, element, index)  # 目标元素

        '''预设key键，预设筛选标识，目标元素值，操作表达式过渡列表'''
        partake_Key = None; partake_Condition = None; value_Obtained = None; tranExpression_List = None
        filterId_List = ['int', 'text', 'date', 'time', 'dateTime']  # 可用筛选标识列表
        '''list -- string'''
        try:
            '''list'''
            tranExpression_List = eval(content)[:3]  # 列表元素个数限定
        except Exception as error:
            '''string'''
            tranExpression_List = [content] if content else ['']
        finally:
            '''处理'''
            tran_Variable = [value for value in tranExpression_List if value in filterId_List]
            if tran_Variable: partake_Condition = tran_Variable[0]; tranExpression_List.remove(partake_Condition)
            try:
                for item in tranExpression_List: 
                    value_Obtained = element_Obtained.get_attribute(item)  # 属性值
                    if value_Obtained: tranExpression_List.remove(item); break
                else:
                    raise Exception
            except:
                value_Obtained = element_Obtained.text  # 文本值
            finally:
                '''通用处理'''
                partake_Key = "".join(tranExpression_List)  # key键

            if not partake_Key: partake_Key = self.logicFunction_Object.beforehand('key_System_date(%Y%m%d_%H%M%S)')  # 默认key键
            if partake_Condition: value_Obtained = self.logicFunction_Object.Regular_takeData(value_Obtained, partake_Condition)[0]  # 数据筛选提取

        trusteeship.info(f"keyword ---getElementText--- : /***  获取到的元素值：{value_Obtained.strip()}  ***/")
        '''序列化对象，将信息存入'''
        PRIVATEDATA['ELEVALUE'][partake_Key] = value_Obtained.strip()


    def takeElementText(self, targeting, element, content=None):
        '''解释：未知属性值比较第二步，取出元素值，进行循环比较'''
        '''
         说明：
            . 适用于删除等界面元素比较操作
            . content：代表元素值操作表达式；可接收三种类型的数据 None/string/List
    
         注：对content参数进行重点解释：
            1、当参数值为空(None)时：代表“参照元素的text文本值”要与“数据文件中最后一个key键对应的value值”进行比对判断。
            2、当参数值为(string)时：关键字可以接收三种操作值中的任意一个 “key键/ attribute何种属性/ reversal是否需要逻辑取反”进行处理。
            3、当参数值为(list)时：可以同时接收三种操作值 [key键、attribute何种属性、reversal是否需要逻辑取反]进行处理。

         注：关键字使用规则解释：
            1、“要进行比较的元素”必须是一个元素列表。(即传入的 targeting 、element 必须是复数定位形式)
            2、当content参数值为list类型时，其中各项可随意书写不需要按照特定顺序书写，关键字会自动进行判别筛选。例如：['value','key_one',True] || [True,'key_one','value']
            3、当content参数值为list类型时，子项个数需要在 2 - 3 个范围内否则无实际意义。例如：['value','key_one'] || ['value', True] || [True,'key_one','value']
            4、不管content为何种参数形式，只要是出现“未指定key键”的情况，关键字则默认将数据文件中最后一个key键对应的value值取出作为断言判断依据。
            5、如果出现 “key键” 与 “attribute何种属性”同名情况时，权重最高的值判定为key键，顺位为属性值。
             · 例如：['value'(判定为key),'value'(判定为属性值)]
            6、如果出现 “重复key键”的情况，则权重最高的判定为key键，顺位为属性值。
             · 例如：['key_One'(判定为key),'key_Two'(判定为属性值)]
            7、[非法]如果出现 “重复属性”的情况，则对给出的所有属性做字符串拼接后，判定为属性值。
             · 例如：['value','onclick']，处理结果为 ['valueonclick'(判定为属性值)]
            8、逻辑取反(传入True代表取反，关键字默认为False)：当“取反状态”时 A!=B抛出错误，当“非取反状态(默认状态)”时 A==B抛出错误。
        '''
        A_elements_Contrast = self.locators(targeting, element)  # 待比对元素(实际元素)

        '''关键字操作表达式列表，key键、属性名、逻辑取反判断'''
        tranExpression_List = None; keyValue = None; attribute = None; reversal = False
        '''string - list'''
        try:
            '''list'''
            content = eval(content)
            tranExpression_List = content[:3]
        except Exception as error:
            '''string'''
            tranExpression_List = [content] if content else ['']
        finally:
            '''处理'''
            tran_keyValue = [value for value in tranExpression_List if value in PRIVATEDATA['ELEVALUE'].keys()]  # key 键
            if tran_keyValue: keyValue = tran_keyValue[0]; tranExpression_List.remove(keyValue)

            tran_reversal = [value for value in tranExpression_List if isinstance(value, bool)]  # reversal 取反
            if tran_reversal: reversal = bool(tran_reversal[0]); tranExpression_List.remove(reversal)

            attribute = "".join(tranExpression_List)  # attribute 属性
        
        if not keyValue: keyValue = [key for key in PRIVATEDATA['ELEVALUE'].keys()][-1]  # key 空值处理

        E_reference_Value = PRIVATEDATA['ELEVALUE'][keyValue]  # 断言参照值(预期结果)
        for element in A_elements_Contrast:
            A_contrast_Value = element.get_attribute(attribute).strip() if attribute else element.text.strip()  # 断言对比值(实际结果)
            trusteeship.info(f"keyword ---takeElementText--- : /***  预期参照值: {E_reference_Value}    实际对比元素值: {A_contrast_Value}  ***/")

            if not self.logicFunction_Object.mutual_in(A_contrast_Value, E_reference_Value) if reversal else A_contrast_Value == E_reference_Value:
                return False
        '''未在循环中跳出'''
        return True


    def gethandle(self):
        '''解释：句柄操作步骤一，获取当前主页面的句柄'''
        windowHandle = self.driver.current_window_handle  # 获取当前窗口句柄
        PRIVATEDATA['HANDLE'].append(windowHandle)
        trusteeship.info(f"keyword ---gethandle--- : /***  句柄获取: {windowHandle}  ***/")


    def enterWindow(self, win_MAX=False):
        '''解释：句柄操作步骤二，跳入弹出的窗口；如果需要将弹出的窗口最大化，win_MAX传入True'''
        handleList = PRIVATEDATA['HANDLE']  # 句柄数据读取
        allhandles = self.driver.window_handles  # 获取所有展开窗口的句柄
        handle = "".join([item for item in allhandles if not(item in handleList)])  # 句柄筛选
        
        self.driver.switch_to_window(handle)
        if bool(win_MAX): self.driver.maximize_window()
        trusteeship.info(f"keyword ---enterWindow--- : /***  句柄跳入: {handle}  ***/")


    def outWindow(self):
        '''解释：句柄操作步骤三，句柄跳出'''
        handleList = handleList = PRIVATEDATA['HANDLE']  # 句柄数据读取
        try: 
            self.driver.close(); self.driver.switch_to_window(handleList[-1]) # 窗口关闭
        except Exception as error:
            self.driver.switch_to_window(handleList[-1])  # 句柄跳出
        handleList.pop(-1)
        PRIVATEDATA['HANDLE'] = handleList
        trusteeship.info(f"keyword ---outWindow--- : /***  句柄暂存: {handleList}  ***/")