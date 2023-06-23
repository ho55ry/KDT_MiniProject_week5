#%%
from bs4 import BeautifulSoup
import requests
from	wordcloud import	WordCloud
from	konlpy.tag import	Okt
from	collections	import	Counter
import	matplotlib.pyplot as	plt
import	platform
from	selenium	import	webdriver
#%%
# 카카오 코딩테스트 문제풀이 크롤링

# 동적 크롤링 
def url_crawling(site,urls):
    driver=webdriver.Chrome('C:\\workspace\\chromedriver')
    driver.get(site)
    driver.implicitly_wait(3)
    search_box =	driver.find_element_by_name('s')
    search_box.send_keys('코딩')
    search_box.submit()
    urls.append(driver.current_url)
    urls.append(driver.current_url.replace('com/','com/page/2/'))
    driver.close() 
    driver.quit()

def link_crawling(site,link_list):
    html=requests.get(site)
    soup= BeautifulSoup(html.text, 'html.parser')
    links=soup.select('article.elementor-post')
    for i in links:
        link_list.append(i.select_one('a')['href'])

def text_crawling(word_list,link):
    req= requests.get(link)
    soup	=	BeautifulSoup(req.text,	'html.parser')
    result=soup.text.replace('\n','').replace('\t','').split(' ')		
    for i in result:
        if i != ' ':
            word_list.append(i)

def	make_wordcloud(word_count,	word_list):
    okt =	Okt()
    sentences_tag =	[]
    #	형태소 분석하여 리스트에 넣기
    for	sentence	in	word_list:
        morph	=	okt.pos(sentence)
        sentences_tag.append(morph)
    noun_list =	[]
    for	sentence1	in	sentences_tag:
        for	word,	tag	in	sentence1:
            if	tag	== 'Noun':
                if word not in ['문제','테스트','번','경우','코딩','의','이','카카오','예','다음','방법','차',
                                '개','각','자전거','것','를','모든','위','이상','가장','해설','요청','중','로',
                                '두','신입','공채','이하','풀이','하나','사용','방','인','아래','모두','대여',
                                '때문','따라서','후','트럭','칸','이용','은','상태','가지','해당','위해','라이언',
                                '해결','더','다른','여소','사항','구','시험','응시','플레이어','명','톡','대한',
                                '어피','즉','결과','이번','메시','최소','징','과','바이크','출제','친구','마지막',
                                '난이도','첫','각각','만약','풀','그','양','여러','오른쪽']:
                    noun_list.append(word)
    #	형태소별 count
    counts	=	Counter(noun_list)
    tags	=	counts.most_common(word_count)

    if	platform.system()	==	'Windows':
        path	=	r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system()	==	'Darwin':		#	Mac	OS
        path	=	r'/System/Library/Fonts/AppleGothic'
    else:
        path	=	r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'
    wc =	WordCloud(font_path=path,	background_color='white',	width=800,	height=600)
    print(dict(tags))
    cloud	=	wc.generate_from_frequencies(dict(tags))
    plt.figure(figsize=(10,	8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

def main():
    urls=[]
    link_list=[]
    word_list=[]
    url_crawling('https://tech.kakao.com/blog/',urls)
    for i in urls:
        link_crawling(i,link_list)
    link_list=link_list[:-2]    # 맨밑에 2페이지는 필요없음
    for i in link_list:
        text_crawling(word_list,i)
    make_wordcloud(100,word_list)


main()


# %%

html=requests.get('https://school.programmers.co.kr/learn/challenges?utm_source=google&utm_medium=cpc&utm_campaign=codingtest_test&utm_content=%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AC%B8%EC%A0%9C&utm_term=&gclid=Cj0KCQiA8t2eBhDeARIsAAVEga1HXPzdjHyroc75WOndeaJuxILsisk6pd_MzbZLGFPX9JOUADCZ-cwaAr0BEALw_wcB&order=recent&page=1')
soup= BeautifulSoup(html.text, 'html.parser')
result=soup.text
print(result.replace('\n',''))


# %%

text=r'D:\EXAM_python\DAY_0131_4주차 팀플\text.txt'
f = open(text, 'r',encoding='utf-8')
text=f.read()
f.close()
text=text.replace('\n','').replace('\t','').split(' ')
def	make_wordcloud(word_count,	title_list):
    okt =	Okt()
    sentences_tag =	[]
    #	형태소 분석하여 리스트에 넣기
    for	sentence	in	title_list:
        morph	=	okt.pos(sentence)
        sentences_tag.append(morph)
    noun_adj_list =	[]
    for	sentence1	in	sentences_tag:
        for	word,	tag	in	sentence1:
            if	tag	== 'Noun':
                if word not in ['번','의','예','개','방','모든','를','위','두','이','코딩','여기','것','명','예시']:
                    noun_adj_list.append(word)
    #	형태소별 count
    counts	=	Counter(noun_adj_list)
    tags	=	counts.most_common(word_count)

    if	platform.system()	==	'Windows':
        path	=	r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system()	==	'Darwin':		#	Mac	OS
        path	=	r'/System/Library/Fonts/AppleGothic'
    else:
        path	=	r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'
    wc =	WordCloud(font_path=path,	background_color='white',	width=800,	height=600)
    print(dict(tags))
    cloud	=	wc.generate_from_frequencies(dict(tags))
    plt.figure(figsize=(10,	8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

make_wordcloud(100,text)
# %%
