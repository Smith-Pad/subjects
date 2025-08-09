import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import AssignmentList from './AssignmentList.jsx'
import './subjects.css'

function App() {
        const [count, setCount] = useState(0)

        return (
                <>
                        <body className="subjects-main-menu-global">
                                Subjects
                                <ul></ul>
                                <AssignmentList />
                        </body>
                </>
        )
}

export default App
