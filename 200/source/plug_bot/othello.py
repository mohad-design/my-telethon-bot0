from pyrogram import Client, filters
import json
from func.othello.methods import *
from func.othello.sql import *

@Client.on_callback_query(filters.regex("^strat-*"))
async def answer_(client, callback_query):
    enemy_id = int(callback_query.data.split("-")[1])
    enemy_name = callback_query.data.split("-")[2]
    my_id = callback_query.from_user.id
    if enemy_id == my_id:
        await callback_query.answer("مينفعش تلاعب نفسك ياذكي.", show_alert=True)
    else:
        keyboard = create_board(my_id, enemy_id, callback_query.from_user.first_name, enemy_name)
        obj = json.loads(str(keyboard))
        manage.insert_into_db(
            callback_query.inline_message_id,
            callback_query.chat_instance,
            callback_query.from_user.first_name,
            enemy_name,
            obj
        )
        await callback_query.edit_message_text("اكتر واحد يجمع كور يكسب.\nBy ؍`𝐬𝐭𝐞𝐯𝐞𝐧 ٭| @Ues_steven .", reply_markup=keyboard)
    manage.delete_obj_all()

@Client.on_callback_query(filters.regex("[0-9]*-[0-9]*"))  
async def answer(client, callback_query):
    data_sql = manage.get_obj_from_db(callback_query.inline_message_id, callback_query.chat_instance)
    board = data_sql[4]['inline_keyboard']
    row_selected, col_selected = list(map(int, callback_query.data.split("-")))
    callback_query_data_text = board[row_selected][col_selected]['text']
    turn = board[8][0]['text']
    next_turn = blue if turn == red else red
    
    if callback_query_data_text == white:
        await callback_query.answer("مينفعش تلعب هنا.", show_alert=True)
    elif callback_query_data_text in [red, blue]:
        await callback_query.answer("المكان مش فاضي يا اعمي.", show_alert=True)
    elif callback_query_data_text == yellow:
        red_id = int(board[9][0]['callback_data'])
        blue_id = int(board[9][1]['callback_data'])
        if (turn == red and callback_query.from_user.id != red_id) or (turn == blue and callback_query.from_user.id != blue_id):
            await callback_query.answer("مش دورك.", show_alert=False)
            return
        # update keyboard before calculating possible blocks
        board[row_selected][col_selected]['text'] = turn
        all_reverse_board = calculate_reverse(board, row_selected, col_selected, turn)
        # calculate possible blocks
        possible_squares = possible_blocks(all_reverse_board, next_turn)
        keyboard_update = update_board(
                board,
                possible_squares,
                row_selected, 
                col_selected, 
                next_turn,
                data_sql[2],
                data_sql[3]
                )
        if len(possible_squares) == 0:
            keyboard_update = who_wins(
                    board,
                    possible_squares,
                    row_selected, 
                    col_selected, 
                    next_turn,
                    data_sql[2],
                    data_sql[3]
                    )    
            manage.delete_obj(callback_query.inline_message_id, callback_query.chat_instance)

        obj = json.loads(str(keyboard_update))
        manage.update_keyboard(callback_query.inline_message_id, callback_query.chat_instance, obj) 
        await callback_query.edit_message_reply_markup(keyboard_update)
