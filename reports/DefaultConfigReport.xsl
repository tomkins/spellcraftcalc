<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml" xmlns:math="http://exslt.org/math" version="1.0">
<xsl:output encoding="iso-8859-1" method="xml" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="DTD/xhtml1-strict.dtd" indent="yes" omit-xml-declaration="yes"/>
<xsl:template name="formatCost">
	<xsl:param name="cost"/>
	<xsl:variable name="plat" select="floor($cost div 10000000)"/>
	<xsl:variable name="gold" select="floor(($cost - $plat * 10000000) div 10000)"/>
	<xsl:variable name="silver" select="floor(($cost - $plat * 10000000 - $gold * 10000) div 100)"/>
	<xsl:variable name="copper" select="floor(($cost - $plat * 10000000 - $gold * 10000 - $silver * 100))"/>
	<xsl:if test="$plat &gt; 0"><xsl:copy-of select="$plat"/>p<xsl:text> </xsl:text></xsl:if>
	<xsl:if test="$gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$gold"/>g<xsl:text> </xsl:text></xsl:if>
	<xsl:if test="$silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$silver"/>s<xsl:text> </xsl:text></xsl:if>
	<xsl:if test="$copper &gt; 0 or $silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0"><xsl:copy-of select="$copper"/>c</xsl:if>
</xsl:template>

<xsl:template name="nl">
<xsl:text>
</xsl:text>
</xsl:template>

<xsl:template match="SLOT">
  <xsl:variable name="slotnum">
    <xsl:value-of select="number(@Number) + 1"/>
  </xsl:variable>
  <xsl:if test="Type != 'Unused'">
    <xsl:choose>
      <xsl:when test="@Type = 'player'">
	<tr>
	  <td>Gem <xsl:copy-of select="$slotnum"/>:</td>
	  <td align="right"><xsl:value-of select="Amount"/></td>
	  <td><xsl:value-of select="Effect"/></td>
	  <td>&#160;- <xsl:value-of select="Qua"/></td>
	  <td><xsl:value-of select="Name"/></td>
	</tr>
      </xsl:when>
      <xsl:otherwise>
	<tr>
	  <td>Slot <xsl:copy-of select="$slotnum"/>:</td>
	  <td align="right"><xsl:value-of select="Amount"/></td>
	  <td><xsl:value-of select="Effect"/></td>
	  <td colspan="2">
	    <xsl:text>&#160;</xsl:text>
	    <xsl:if test="@Type = 'effect'">
	      <xsl:text>- </xsl:text><xsl:value-of select="Name"/>
	    </xsl:if>
	  </td>
	</tr>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:if>
</xsl:template>

<xsl:template match="SCItem">
  <xsl:if test="count(SLOT) &gt; 0 and Equipped = '1'">
    <dl>
      <dt><b><xsl:value-of select="Location" /></b></dt>
      <dt>Name: <xsl:value-of select="ItemName"/></dt>
      <dt>
	<xsl:text>Level: </xsl:text><xsl:value-of select="Level"/>
	<xsl:text> &#160; Quality: </xsl:text><xsl:value-of select="ItemQuality"/>
	<xsl:text> &#160; AF/DPS: </xsl:text><xsl:value-of select="AFDPS"/>
	<xsl:text> &#160; Bonus: </xsl:text><xsl:value-of select="Bonus"/>
      </dt>
      <xsl:if test="ActiveState = 'player'">
	<dt>
	  <xsl:text>Imbue Points: </xsl:text><xsl:value-of select="Imbue"/>
	  <xsl:text> of </xsl:text><xsl:value-of select="ItemImbue"/>
	  <xsl:text> &#160; Quality: </xsl:text><xsl:value-of select="ItemQuality"/>
	  <xsl:text> &#160; Overcharge: </xsl:text><xsl:value-of select="Overcharge"/>
	</dt>
      </xsl:if>
      <dt>
	<table>
	  <xsl:apply-templates select="SLOT"/>
	</table>
      </dt>
      <dt>
	<xsl:text>Utility: </xsl:text><xsl:value-of select="Utility"/>
        <xsl:if test="ActiveState = 'player'">
	  <xsl:text> &#160; SC Cost: </xsl:text>
	  <xsl:call-template name="formatCost">
	    <xsl:with-param name="cost" select="Cost"/>
	  </xsl:call-template>
	  <xsl:text> &#160; SC Price: </xsl:text>
	  <xsl:call-template name="formatCost">
	    <xsl:with-param name="cost" select="Price"/>
	  </xsl:call-template>
        </xsl:if>
      </dt>
    </dl>
    <br />
  </xsl:if>
</xsl:template>

<xsl:template match="/SCTemplate">
  <xsl:variable name="lowercase" select="'abcdefghijklmnopqrstuvwxyz'" />
  <xsl:variable name="uppercase" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ'" />
  <body>
  <center><b>Config Report</b></center><br />
  <center><b>Stats</b></center><hr />
  <table cellspacing="10" cellpadding="0">
    <xsl:for-each select="Stats/*">
      <xsl:if test="name() != 'Acuity'">
	<xsl:if test="position() = 1 or position() = 5 or position() = 10">
	  <xsl:text disable-output-escaping="yes">&lt;tr&gt;</xsl:text>
	</xsl:if>
	<xsl:choose>
	  <xsl:when test="name() = 'Hits'">
	    <td>Hits:</td>
	  </xsl:when>
	  <xsl:when test="name() = 'Power'">
	    <td>Pow:</td>
	  </xsl:when>
	  <xsl:when test="name() = 'PowerPool'">
	    <td>%PP:</td>
	  </xsl:when>
	  <xsl:otherwise>
   	    <td><xsl:value-of select="translate(substring(name(),1,3), $lowercase, $uppercase)"/>:</td>
	  </xsl:otherwise>
	</xsl:choose>
	<td>
	  <xsl:value-of select="TotalBonus"/>
	  <xsl:if test="name() = 'PowerPool'"><xsl:text>%</xsl:text></xsl:if>
	  <xsl:text> / </xsl:text>
	  <xsl:value-of select="BaseCap + CapBonus"/>
	</td>
	<xsl:if test="position() = 0 or position() = 4 or position() = last()">
	  <xsl:text disable-output-escaping="yes">&lt;/tr&gt;</xsl:text>
	  <xsl:call-template name="nl"/>
	</xsl:if>
      </xsl:if>
    </xsl:for-each>
  </table>
  <br />
  <center><b>Resists</b></center>
  <hr />
  <table cellspacing="10" cellpadding="0">
    <xsl:for-each select="Resists/*">
      <xsl:if test="position() mod 3 = 1">
	<xsl:text disable-output-escaping="yes">&lt;tr&gt;</xsl:text>
      </xsl:if>
      <td><xsl:value-of select="name()"/>:</td>
      <td>
	<xsl:value-of select="TotalBonus"/>
	<xsl:text> / </xsl:text>
	<xsl:value-of select="BaseCap"/>
	<xsl:for-each select="RacialBonus">
	  <xsl:text> (+</xsl:text><xsl:value-of select="."/><xsl:text>)</xsl:text>
	</xsl:for-each>
      </td>
      <xsl:if test="position() mod 3 = 0 or position() = last()">
	<xsl:text disable-output-escaping="yes">&lt;/tr&gt;</xsl:text>
      </xsl:if>
    </xsl:for-each>
  </table>
  <br />
  <xsl:for-each select="Skills|Focus|OtherBonuses|PvEBonuses">
    <xsl:if test="math:max(./*/TotalBonus) &gt; 0">
      <center><b><xsl:value-of select="name()"/></b></center><hr />
      <table>
	<xsl:for-each select="./*">
	  <tr>
	    <td align="right"><xsl:value-of select="TotalBonus"/></td>
	    <td> / <xsl:value-of select="BaseCap"/></td>
	    <td>&#160;<xsl:value-of select="name()"/></td>
	  </tr>
	</xsl:for-each>
      </table>
      <br />
    </xsl:if>
  </xsl:for-each>
  <center><b>Piece Listing</b></center>
  <hr />
  <xsl:apply-templates select="SCItem"/>
</body>
</xsl:template>
</xsl:stylesheet>
