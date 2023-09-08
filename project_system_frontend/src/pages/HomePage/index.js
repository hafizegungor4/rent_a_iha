import {Link} from "react-router-dom";

export const HomePage = () => {

   return <>
        <h1>HomePage</h1>
        <br/>
        <Link to={"/iha"}>İha</Link>
        <br/>
        <Link to={"/rentiha"}>Rent a İha</Link>
        <br/>
        <Link to={"/rentstate"}>Rent State</Link>
        <br/>
       <br/>
        <Link to={"/rentihareport"}>Rent a İha Report</Link>
        <br/>

    </>
}