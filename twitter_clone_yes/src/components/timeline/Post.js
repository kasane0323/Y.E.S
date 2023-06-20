import { ChatBubbleOutline, FavoriteBorder, PublishOutlined, Repeat, VerifiedUser } from '@mui/icons-material'
import { Avatar } from '@mui/material'
import React from 'react'
import Imagebukkoro from './bukkoro.png';
import "./Post.css";

function Post() {
  return (
    <div className='post'>
      <div className='post--avatar'>
        <Avatar ></Avatar> {/* src ={} アバターに画像を入れる */}
        <div className='post--body'>
          <div className='post--header'>
            <div className='post--headerText'>
              <h3>sampleブッコロー</h3>
                <span className="post--headerSpecial">
                  <VerifiedUser className="post--badge" />
                  @bukkoro_sample
                </span>
            </div>
            <div className='post--headerDescription'>
              <p>サンプルツイート！画像転載はゆるさない！サンプルツイート</p>
            </div>
          </div>
          <img className='timeline--title-logo' src={Imagebukkoro} alt="Image"/>
          <div className='post--footer'>
            <ChatBubbleOutline fontSize='small' />
            <Repeat fontSize='small'/>
            <FavoriteBorder fontSize='small'/>
            <PublishOutlined fontSize='small'/>
          </div>
        </div>

      </div>
      
    </div>
  )
}

export default Post
