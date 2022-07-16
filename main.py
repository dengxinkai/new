import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum


class Book(BaseModel):
    name: str
    genre: Literal["fiction", "non-fiction"]
    price: float
    book_id: Optional[str] = uuid4().hex


BOOKS_FILE = "books.json"
BOOKS = []

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOKS = json.load(f)

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root():
    return [{"id":1,"name": """根据本次交易进展，公司根据《证券法》以及《上市公司重大资产重组管理 办法》等相关法律法规及其他规范性文件要求对《上海皓元医药股份有限公司发 行股份及支付
买资产并募集配套资金暨关联交易报告书(草案)》及其摘 要部分内容进行了补充修订。
表决结果:5 名赞成，占全体无关联董事人数的 100%;0 名弃权，0 名反对。 郑保富先生、高强先生、李硕梁先生、金飞敏先生为本交易事项的关联董事，依 法回避表决。"""},{"id":2,"name": """
然而，由於需要更多時間安排從中國匯款至香港，本公司預計末期股息將改為 於2022年7月25日 或 之 前 派 付。
除上文所披露者外，所有其他載於該通函有關派付末期股息的資料維持不變。
 中 國，北 京，2022年7月13日
承董事會命
北京市春立正達醫療器械股份有限公司
董事長
史文玲
於 本 公 告 日 期，本 公 司 執 行 董 事 為 史 春 寶 先 生、岳 術 俊 女 士、解 鳳 寶 先 生 及 史文玲女士;本公司非執行董事為王鑫先生;及本公司獨立非執行董事為葛長 銀 先 生、黃 德 盛 先
及 翁 杰 先 生。"""},{"id":3,"name": """中国南玻集团股份有限公司(以下简称“公司”)董事会于2022年7月12日 收到公司第一大股东前海人寿保险股份有限公司《关于提请董事会召开临时股东 大会的函
现对函件内容公告如下:
前海人寿保险股份有限公司(以下简称“前海人寿”、“提案人”)持有中 国南玻集团股份有限公司(以下简称“上市公司”、“公司”或“南玻集团”) 10%以上的股份。
根据《中国南玻集团股份有限公司章程》的规定，单独或者合计持有公司10% 以上股份的股东有权向董事会提请召开临时股东大会。
鉴于目前公司董事席位空缺，且2022年7月8日公司召开的临时董事会表决未 通过《关于补选公司第九届董事会董事的议案》和《关于召开2022年第三次临时 股东大会的议案》，为规范上市公司治理，确保
常运行，前海人寿 作为单独持股10%以上的股东，依法向南玻集团董事会提议于2022年8月9日前召"""},{"id":4,"name": """本公司股票将于 2022 年 7 月 15 日在深圳证券交易所上市。本公司提醒投资 
充分了解股票市场风险及本公司披露的风险因素，在新股上市初期切忌盲目 跟风“炒新”，应当审慎决策、理性投资。
如无特别说明，本上市公告书中的简称或名词的释义与本公司首次公开发行 股票招股说明书中的相同。如本上市公告书中合计数与各加数直接相加之和在尾 数上存在差异，系四舍五入所致。"""},{"id":5,"name":
"""二、监事会会议审议情况经与会监事充分讨论，本次会议以记名投票方式审议通过了如下议案:一)审议通过《关于<上海皓元医药股份有限公司发行股份及支付现金购 买资产并募集配套资金暨关联交易报告书(草案)(修订稿)>及其摘要的议案》根据本次交易进展，公司根据《证券法》以及《上市公司重大资产重组管理 办法》等相关法律法规及其他规范性文件要求对《上海皓元医药股份有限公司发 行股份及支付现金购买资产并募集配套资金暨关草案)》及其摘 要部分内容进行了补充修订。表决结果:3 名赞成，占全体监事人数的 100%;0 名弃权，0 名反对。体内容详见公司于同日在上海证券交易所网站(www.sse.com.cn)披露的 《上海皓元医药股份有限公司发行股份及支付现金购买资产并募集配套资金暨"""},{"id":6,"name": """中国南玻集团股份有限公司
简称“公司”)董事会于2022年7月12日 收到公司第一大股东前海人寿保险股份有限公司《关于提请董事会召开临时股东 大会的函》，现对函件内容公告如下:
前海人寿保险股份有限公司(以下简称“前海人寿”、“提案人”)持有中 国南玻集团股份有限公司(以下简称“上市公司”、“公司”或“南玻集团”) 10%以上的股份。
根据《中国南玻集团股份有限公司章程》的规定，单独或者合计持有公司10% 以上股份的股东有权向董事会提请召开临时股东大会。
鉴于目前公司董事席位空缺，且2022年7月8日公司召开的临时董事会表决未 通过《关于补选公司第九届董事会董事的议案》和《关于召开2022年第三次临时 股东大会的议案》，为规范上市公司治理，确保
常运行，前海人寿 作为单独持股10%以上的股东，依法向南玻集团董事会提议于2022年8月9日前召"""}]


@app.get("/random-book")
async def random_book():
    return random.choice(BOOKS)


@app.get("/list-books")
async def list_books():
    return {"books": BOOKS}


@app.get("/book_by_index/{index}")
async def book_by_index(index: int):
    if index < len(BOOKS):
        return BOOKS[index]
    else:
        raise HTTPException(404, f"Book index {index} out of range ({len(BOOKS)}).")


@app.post("/add-book")
async def add_book(book: Book):
    book.book_id = uuid4().hex
    json_book = jsonable_encoder(book)
    BOOKS.append(json_book)

    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOKS, f)

    return {"book_id": book.book_id}


@app.get("/get-book")
async def get_book(book_id: str):
    for book in BOOKS:
        if book.book_id == book_id:
            return book

    raise HTTPException(404, f"Book ID {book_id} not found in database.")
