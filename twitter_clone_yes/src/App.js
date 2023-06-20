import { Height, InstallDesktop } from '@mui/icons-material';
import { height, maxHeight } from '@mui/system';
import "./App.css";
import Timeline from './components/timeline/Timeline';

function App() {
  return (
    <div className="app">
      {/* Time line*/}
      <Timeline />
    </div>
  );
}


export default App;