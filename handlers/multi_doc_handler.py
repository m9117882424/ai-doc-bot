import os
import tempfile
from aiogram import types, Dispatcher
from tg_api import get_file_download_url
from utils.ocr_utils import extract_text_from_file
from gpt_parser import process_document
from utils.excel_export import save_data_to_excel
import openpyxl
from openpyxl.styles import Font

# Храним временные сессии пользователей
user_sessions = {}

def create_excel_from_batch(data_list, output_path):
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Batch Results"
    ws.append(["№", "Тип", "doc_id", "date", "amount", "status"])
    for cell in ws[1]:
        cell.font = Font(bold=True)

    for idx, data in enumerate(data_list, start=1):
        ws.append([
            idx,
            data.get("document_type", ""),
            data.get("doc_id", ""),
            data.get("date", ""),
            data.get("amount", ""),
            data.get("status", "ok")
        ])

    wb.save(output_path)

async def handle_document_multi(msg: types.Message):
    user_id = msg.from_user.id
    user_sessions.setdefault(user_id, [])

    try:
        file_info = await msg.bot.get_file(msg.document.file_id)
        file_name = msg.document.file_name
        temp_path = os.path.join(tempfile.gettempdir(), f"{user_id}_{file_name}")

        await msg.bot.download_file(file_info.file_path, destination=temp_path)
        ocr_text = extract_text_from_file(temp_path)
        result = process_document(ocr_text)

        if "error" in result:
            result = {
                "document_type": "unknown",
                "doc_id": "",
                "date": "",
                "amount": "",
                "status": "error"
            }

        user_sessions[user_id].append(result)
        await msg.answer(f"✅ Файл обработан. Загружено файлов: {len(user_sessions[user_id])}")

        os.remove(temp_path)

    except Exception as e:
        await msg.answer(f"❌ Ошибка при обработке: {str(e)}")

async def finish_batch(msg: types.Message):
    user_id = msg.from_user.id
    batch = user_sessions.get(user_id, [])

    if not batch:
        await msg.answer("⚠️ Нет загруженных документов.")
        return

    output_excel = os.path.join(tempfile.gettempdir(), f"batch_result_{user_id}.xlsx")
    create_excel_from_batch(batch, output_excel)

    await msg.answer_document(types.FSInputFile(output_excel), caption="📊 Итоговый файл.")
    os.remove(output_excel)
    user_sessions[user_id] = []

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_document_multi, content_types=types.ContentType.DOCUMENT)
    dp.register_message_handler(finish_batch, commands=["finish"])