import { Avatar, Button } from '@mui/material'
import React from 'react'
import './TweetBox.css';


function TweetBox() {
  return (
    <div className='tweetBox'>
      <form>
        <div className='tweetBox--input'>

          {/* プロフィールアイコン */}
          <Avatar />

          {/* ツイート入力画面 */}
          <input placeholder='いまどうしてる？'type='text'></input>
        </div>

        {/* 画像挿入画面 */}
        <input className='tweetBox--imageInput' placeholder='画像のURLを入力してください' type='text'></input>

        <Button className='tweetBox--tweetButton' type='submit'>ツイート</Button>

      </form>
    </div>
  )
}

export default TweetBox
