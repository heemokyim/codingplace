package storage;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

/**DataBase의 설정을 적어둔 connection.properties를 읽어들여 DB와의 Connection
 * 을 만드는 Class.*/
public class Connector {
	
	public static Connection getConnection(String propFile){
		Connection conn = null;
		Properties prop = new Properties();
		
		/*properties 속성 값들을 propFile로 부터 가져온다.*/
		try {
			prop.load(Thread.currentThread().getContextClassLoader().getResourceAsStream(propFile));
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		/*Load the Driver class
	     *jdbc.driver 속성으로 기재된 값을 가져와 JDBC driver를 셋팅한다.*/
	    String driver = prop.getProperty("jdbc.driver") ;
	    try {
	    	Class.forName(driver);
	    }
	    catch (ClassNotFoundException e) {
	    	e.printStackTrace() ;
	    }

	    /*Try to make a connection
	     *jdbc.url 속성으로 기재된 값을 가져와 JDBC driver를 이용 DB와 프로그램의 Connection을 생성한다.*/
	    String dbURL = prop.getProperty("jdbc.url") ;
	    try{
	    	conn = DriverManager.getConnection(dbURL) ;
	    }
	    catch (SQLException e) {
	    	e.printStackTrace() ;
	    }
		
		return conn;
	}
}	
