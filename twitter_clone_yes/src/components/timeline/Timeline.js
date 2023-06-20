import React from 'react'
import TwitterIcon from '@mui/icons-material/Twitter';
import Image from './YES_logo.png';
import "./Timeline.css";
import TimelineOption from "./TimelineOption";
import TweetBox from './TweetBox';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import Post from './Post';


function Timeline() {
  return (
    <div className='timeline'>

      {/* Heder */} 
        <div className='timeline--header'>
          <TimelineOption />
        
          {/* Twitterアイコン */}
          <TwitterIcon className='timeline--TwitterIcon'/>

          {/* サイトタイトル */}
          <img className='timeline--title-logo' src={Image} alt="Image" />

          {/* メニューアイコン */}
          <MoreVertIcon className='timeline--menuIcon'/>

        </div>

        <div className='timeline--tweet'>
          {/*TweetBox */}
          <TweetBox />
          

          {/* Post */}
          <Post />
          <Post />
          <Post />
          <Post />
          <Post />
        </div>

    </div>
  )
}

export default Timeline