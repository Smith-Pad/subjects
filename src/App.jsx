import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import AssignmentList from './AssignmentList.jsx'
import './subjects.css'

function App() {
        const [count, setCount] = useState(0)

        return (
                <>
                        <body class="subjects-main-menu-global">
                                <div class="subjects-title">
                                        Subjects
                                        <div class="header-buttons">
                                                <button class="subjects-button-1">Back</button>
                                                <button class="subjects-button-1 color-is-red">Ask Para</button>
                                        </div>
                                </div>
                        </body>
                </>
        )
}

export default App
